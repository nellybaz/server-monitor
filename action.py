import sys
import os
from datetime import datetime
import urllib
import smtplib



dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = dir_path +"/data.txt"
dir_path += "/email.txt"

f=open(dir_path, "a+")
data = open(data_path, "r")


server = 'https://w3schools.com'


email = ""
for i, d in enumerate(data):
    if i == 0:
        email = d
    elif i == 1:
        server = d

data.close()

res = urllib.urlopen(server)

message = '\nSERVER REQUEST FOR '+ server + ' \nDATE: ' +str(datetime.now()) + ' \nSTATUS CODE: '+ str(res.getcode())


try:
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login('nellybaz10@gmail.com', 'nextlevel5')


   #Send the mail
    msg = "\nHello! \n " + message # The /n separates the message from the headers
    s.sendmail("nellybaz10@gmail.com", email, msg)
    s.quit()
except:
    f.write("Error occured \n")    

f.write(message)
f.close()



