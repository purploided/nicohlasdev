# #basic ip logger for websites, dont skid or you have down syndrome
#  #i had to make mods to "pythonpinger" for this, send help
#   #~nicolas

import sys
import subprocess
import time
from termcolor import colored
from subprocess import run

def delete_last_line(): #thanks stackoverflow

    "Use this function to delete the last line in the STDOUT"

    sys.stdout.write('\x1b[1A')

    sys.stdout.write('\x1b[2K')

#queue
print("M")
time.sleep(0.2)
delete_last_line()
print("Ma")
time.sleep(0.2)
delete_last_line()
print("Mad")
time.sleep(0.2)
delete_last_line()
print("Made")
time.sleep(0.2)
delete_last_line()
print("Made b")
time.sleep(0.2)
delete_last_line()
print("Made by")
time.sleep(0.2)
delete_last_line()
print("Made by N")
time.sleep(0.2)
delete_last_line()
print("Made by Ni")
time.sleep(0.2)
delete_last_line()
print("Made by Nic")
time.sleep(0.2)
delete_last_line()
print("Made by Nico")
time.sleep(0.2)
delete_last_line()
print("Made by Nicol")
time.sleep(0.2)
delete_last_line()
print("Made by Nicola")
time.sleep(0.2)
delete_last_line()
print("Made by Nicolas")
time.sleep(0.5)
delete_last_line()

time.sleep(1)
#just prints "info logger"
print(colored(''' _         __             _       __ _  __ _           
(_) _ _   / _| ___       | | ___ / _` |/ _` | ___  _ _ 
| || ' \ |  _|/ _ \      | |/ _ \\__. |\__. |/ -_)| '_|
|_||_||_||_|  \___/      |_|\___/|___/ |___/ \___||_|  
''', "green"))

time.sleep(1)

delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()

#the cli, custom made
print(colored("---[1] webnamping.py", "green"))
time.sleep(0.5)
print(colored("------#", "green"))
time.sleep(0.5)
openyesyes = input(colored("--------Which file would you like to start? ", "green"))

#literally just press 1
if openyesyes == ("1"):
    run('python webnamping.py')
#
#
    time.sleep(10000)