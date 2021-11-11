# #im not giving you the mods i made to pythonping, customize it yourself
#  #i spent too much time
#   #too much time on my hands man
#    #stop reading this and run the code mate
#     #~nicolas   

import time
import socket
import pythonping
from termcolor import colored
from pythonping import ping
    # defines my laziness, pretty self explanitory
def webnam():                                            
    webname = input(colored("Which web address would you like to log? ", "green"))
    askping = input(colored("Would you like to ping the website too? ", "green"))
    if askping == ("Yes"):
        # be a skid, steal this code, u wont
        pinglog = ping(webname, count=1)
        print("#")
        print("Info logging", webname)
        print("#")
        time.sleep(0.5)
            # prints out basic knowledge that nobody will use
        print("Address:", webname)
        print("IP:", socket.gethostbyname(webname))
        print("Response Time:", pinglog)
                # now we get shit
    elif askping == ("No"):
        print("Info logging", webname)
        print("#")
                    # now we get shit (w/o the response time)
        print("Address:", webname)
        print("IP:", socket.gethostbyname(webname))
        print("#")
                        # fuckin read the code, you know what this does
webnam()