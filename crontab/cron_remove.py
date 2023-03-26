from crontab import CronTab

# Create a new crontab object
cron = CronTab(user='your_username')

# Iterate over all cron jobs and remove the one with a specific command
for job in cron:
    if job.command == '/path/to/your/command':
        cron.remove(job)

# Write the changes to the crontab
cron.write()
