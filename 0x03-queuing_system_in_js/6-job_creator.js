const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
  phoneNumber: 'string',
  message: 'string',
};

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log('Notification job completed', job.id);
  } else {
    console.log('Notification job failed');
  }
});
job.on('complete', () => console.log('Notification job completed'));
