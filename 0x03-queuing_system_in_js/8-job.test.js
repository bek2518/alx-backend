import createPushNotificationsJobs from './8-job.js';
import kue from 'kue';
const { expect } = require('chai');

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit()
  })

  it('display a error message if jobs is not an array', () => {
    expect(createPushNotificationsJobs({}, queue)).to.throw;
  })

  it('Create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4154318781',
        message: 'This is the code 4562 to verify your account'
      },
      {
        phoneNumber: '4151218782',
        message: 'This is the code 4321 to verify your account'
      },
    ]
    createPushNotificationsJobs(jobs, queue);
  })
});
