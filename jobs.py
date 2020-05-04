from crontab import CronTab
import os
import getpass


user = getpass.getuser()
os.system("echo USERNAME PROCESS IS RUNNING ON IS " + user)

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += "/action.py"

cron = CronTab(user=str(user))
job = cron.new(command='python '+dir_path)
job.minute.every(1)

cron.write()