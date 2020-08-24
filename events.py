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

    """Does all the work for the urban dictionary module, more tweaks to this will be coming next"""
    """def urbdict(self, irc_text):
        try:
            define_word = irc_text.split('.ud ',1)[1].split()
            if define_word == []:
                raise IndexError
            else:
                joined_search = " ".join(define_word)
                ds.url_modifier(joined_search)
                ds.parse_soup(ds.full_link)
                ds.html2text_convert(ds.string_definition)
                if len(ds.converted_text) > 439:
                    self.event_output = "Definition too long for IRC. Here is a link: {}".format(ds.full_link)
                else:
                    self.event_output = ds.converted_text
        except (IndexError):
            self.event_output = "you need to enter .ud [search term] to make this work...scub"
        except(UnicodeEncodeError):
            self.event_output = "Get that unicode shit out of here!"
"""
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

