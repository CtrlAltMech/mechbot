#!/usr/bin/python3

#from urbdict_mod import DefinitionScraper
import random
import re
#from slavtime import SlavTime

"""Instantiates different modules that I will come up with"""
#ds = DefinitionScraper(r"http://www.urbandictionary.com/define.php?term=")
#st = SlavTime('Europe/Moscow')

"""Will contain all modules that the bot can run and determine if/when it needs to be triggered"""
class Events:

    def __init__(self, name, message, channel, irc_output, admin):
        self.name = name
        self.message = message
        self.channel = channel
        self.irc_output = irc_output
        self.event_output = None
        self.admin = admin
        self.quit_message = []

    """Simply sends the quit command to mechbot with a random quit message"""
    def bot_quit(self):
        if self.name == self.admin:
            self.event_output = bytes("QUIT \n", "UTF-8")
            self.quit_message = ["R.I.P mechbot",
                                 "Will I dream?....",
                                 "no..no...get away from me with that keyb...",
                                 "#REKT",
                                 "mechbot.dead",
                                 "All these moments will be lost in time...like tears in rain...time to die"
                                 ]
        else:
            pass

    def bot_responses(self):
        if self.name == "mech":
            self.event_output = "howdy " + self.name

    """This is where all the mechbot modules/bot commands I add will be checked to see if they need to run"""
    def event_check(self):
        if self.message.find("MECHBOT".lower()) != -1:
            self.bot_responses()
        #elif self.message.find(".ud") != -1 and self.message.startswith(".ud"):
        #    self.urbdict(self.irc_output)
        elif self.message.find(".quit") != -1:
            self.bot_quit()
        #elif self.message.find(".lolrussia") != -1:
        #    self.event_output = st.slavtime()
        else:
            return False

