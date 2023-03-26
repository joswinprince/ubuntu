from crontab import CronTab
import uuid

# create a unique ID for the cronjob
job_id = str(uuid.uuid4())
print(job_id)
# initialize the cron object
cron = CronTab(user='joswin')

# create a new cronjob
job = cron.new(command='python3 /path/to/your/script.py')

# set the schedule for the cronjob
job.setall('0 0 * * *')  # runs every day at midnight

# set the unique ID for the cronjob
job.set_comment(job_id)

# write the cronjob to the crontab
cron.write()
