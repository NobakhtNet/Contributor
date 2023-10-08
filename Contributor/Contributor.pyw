from os import chdir, path
from datetime import date
from sys import exit

# execute code where the current folder is:
input(path.dirname(path.abspath(__file__)))

# execute code once a day:
with open("date.txt", "r") as time:
    if time.read() == str(date.today()):
        exit(0)
    else:
        with open("date.txt", "w") as txt:
            txt.write(str(date.today()))

from time import sleep
from requests import head, ConnectionError
from getSetting import *

# check if client is connected to internet
connected = True
for x in range(tries):
    try:
        head("http://google.com", timeout=5)
        break
    except ConnectionError:
        connected = False
        sleep(minutes * 60)

if not connected:
    exit(0)

from subprocess import run
from random import randint

# count of contribution for today:
conCount = randint(min, max)

if conCount == 0:
    exit(0)

# execute code where the repository folder is:
chdir(repLoc)

# update the text file then commit and push the repository multiple times:
for count in range(1, conCount + 1):
    with open(txtLoc, "w") as txt:
        txt.write("Today's update count: " + str(count))

    run(
        'git add -A && git commit -m "Updated" && git push -u -f origin main',
        shell=True,
    )
