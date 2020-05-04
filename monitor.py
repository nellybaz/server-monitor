#!/usr/bin/env python3

import os
import sys


# Checking for the parameters given
if len(sys.argv) < 2:
    os.system("All parameters are needed")
    sys.exit()

# Get the server from the first param
server = sys.argv[1]

# Get the email from the second params
email = sys.argv[2]

# Checking if email is valid
if "@" not in email or "." not in email:
    os.system("echo ERROR: email is not valid =====")
    sys.exit()

os.system("echo ===== INSTALLING DEPENCIES FOR SERVER MONITOR =====")
# Install all dependencies this program needs
os.system("pip install -r requirements.txt")


# Ping the server
# os.system("ping www.google.com")

os.system("sudo python jobs.py")

try:
    if sys.argv[2] == "p":
        os.system("git push")
except BaseException:
    pass
    