import { promisify } from 'util';
import { createClient } from 'redis';

const kue = require('kue');
const express = require('express');

const app = express();
const hostname = '0.0.0.0';
const port = 1245;

const client = createClient();
const queue = kue.createQueue();

function reserveSeat(number) {
  return promisify(client.set).bind(client)('availableSeats', number);
}

reserveSeat(50);

function getCurrentAvailableSeats() {
  return promisify(client.get).bind(client)('availableSeats');
}

let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }
  const job = queue.create('reserve_seat', { seat: 1 }).save((error) => {
    if (error) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
      job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
      });
      job.on('failed', (error) => {
        console.log(`Seat reservation job ${job.id} failed: ${error}`);
      });
    }
  });
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    const seat = Number(await getCurrentAvailableSeats());
    if (seat === 0) {
      reservationEnabled = false;
      done(Error('Not enough seats available'));
    } else {
      reserveSeat(seat - 1);
      done();
    }
  });
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
