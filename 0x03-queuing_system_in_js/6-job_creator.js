import kue from 'kue'
const push_notification_code = kue.createQueue()

const jobData = {
  phoneNumber: string,
  message: string,
}

const job = push_notification_code.create('email', jobData).save((err) => {
if (err) console.log('Notification job failed')
if (!err) console.log('Notification job created: ', job.id)
console.log('Notification job completed')
        })
