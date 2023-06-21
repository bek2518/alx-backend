function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    return (new Error('Jobs is not an array'));
  }
  for (const jobData of jobs) {
    const job = queue.create('push_notification_code_3', jobData).save((err) => {
      if (!err) {
        console.log('Notification job created:', job.id);
      }
    });
    job.on('failed', (err) => console.log(`Notification ${job.id} failed: ${err}`));
    job.on('complete', () => console.log(`Notification job ${job.id} completed`));
    job.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% completed`));
  }
}

module.exports = createPushNotificationsJobs;
