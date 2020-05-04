import sys
import os
from datetime import datetime
import urllib


dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += "/email.txt"


server = 'https://w3schools.com'
res = urllib.urlopen(server)

message = '\nSERVER REQUEST FOR '+ server + ' \nDATE: ' +str(datetime.now()) + ' \nSTATUS CODE: '+ str(res.getcode())

f=open(dir_path, "a+")

f.write(message)
f.close()