#!/usr/bin/env python3

### Handles all things network connections to do with the bot, improvments to come ###

#TODO Add like any sort of fucking error handling, it bork not gracefully when everything is not perfect
import socket
from time import sleep

class Connections:

    """Takes all the basic information for your bot and initializes it"""
    def __init__(self, server, channel, botnick, port):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ircmsg = ""
        self.server = server
        self.channel = channel
        self.botnick = botnick
        self.port = port
    """Handles the connection, its very basic right now and needs a lot more error handling and other functionality"""
    def connect(self):
        self.irc.connect((self.server, self.port))
        sleep(1)
        self.irc.send(bytes("NICK "+self.botnick+"\r\n","UTF-8"))
        while 1:
            self.ircmsg = self.irc.recv(2048).decode("UTF-8")
            self.ircmsg = self.ircmsg.strip('\r\n')
            print(self.ircmsg)
            if self.ircmsg.find("PING :") != -1:
                code_split = self.ircmsg.split()[1]
                print("PONG "+code_split+" You don't have to yell!")
                self.irc.send(bytes("PONG "+code_split+"\r\n", "UTF-8"))
                break
            else:
                pass 
        sleep(1)
        self.irc.send(bytes("USER "+self.botnick+" "+self.botnick+" "+self.botnick+" :"+self.botnick+"\r\n","UTF-8"))

    """Handles joining the channel and printing to console until the channel/s is joined"""
    def joinchan(self):
        self.irc.send(bytes("JOIN "+self.channel+"\r\n", "UTF-8"))

        while self.ircmsg.find("End of /NAMES list.") == -1:
            self.ircmsg = self.irc.recv(2048).decode("UTF-8")
            self.ircmsg = self.ircmsg.strip('\n\r')
            print(self.ircmsg)

    """This gets called anytime the server sends out a ping message so the bot stays connected"""
    def ping_pong(self, code):
        code_split = code.split()[1]
        print("PONG "+code_split+" Listening....")
        self.irc.send(bytes("PONG " + code_split + "\r\n", "UTF-8"))

    """Basic function to send text to the IRC channel chosen or send messages to IRC console"""
    def sendmsg(self, msg, channel):
        self.irc.send(bytes("PRIVMSG "+channel+" :"+msg+"\n", "UTF-8")) #TODO put this out into the event worker which should handle printing
