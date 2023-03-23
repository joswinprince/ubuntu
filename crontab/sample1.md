```
from crontab import CronTab
  
cron=CronTab(user="joswin")
  
job1=cron.new(command="python3 test1.py >> log1.log 2>&1")
job1.minute.every(2)
  
job2=cron.new(command="python3 test2.py >> /home/joswin/pythonscript/log2.log 2>&1")
job2.minute.every(1)
  
cron.write()

```
