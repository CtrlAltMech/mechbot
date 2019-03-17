#!/usr/bin/python3

### Basic ircbot project known as mechbot that I will be using to further what little python skill I have ###

from connections import Connections
from events import Events
import random

def main():
    """ Initializes the connection and joins the channels listed and sets all other variables"""
    irc = Connections("insert server name","insert channel name","name of bot",6667)
    irc.connect()
    irc.joinchan()
    while 1:

        """Prints all IRC data to console"""
        ircmsg = irc.irc.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

        """Looks for user text and splits it up into all the major parts to be used elsewhere"""
        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!',1)[0][1:]
            message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
            channel = ircmsg.split("PRIVMSG")[1].split(":")[0].strip()

            """Looks through the Event class to determine if there is an event to trigger"""
            event = Events(name,message,channel,ircmsg,"mech")
            event.event_check()
            if event.event_check() == False:
                pass
            else:
                """Determines if the bot is trying to print to IRC or complete a bot specific command QUIT/JOIN etc."""
                try:
                    irc.sendmsg(event.event_output, channel)
                except(TypeError):
                    if event.event_output == bytes("QUIT \n", "UTF-8"):
                        irc.sendmsg(random.choice(event.quit_message), channel)
                        irc.irc.send(event.event_output)
                        break
                    else:
                        pass
        else:
            """Pings back to IRC to let it know I am still listening"""
            if ircmsg.find("PING :") != -1:
                irc.ping_pong(ircmsg)

if __name__ == "__main__":
    main()


