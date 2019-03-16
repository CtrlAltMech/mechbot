#!/usr/bin/python3

# Module for showing time in i7's part of the world

import os, time

class SlavTime:

    # tz code can be changed in the events class. Codes can be found @ https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    def __init__(self, tz):
        self.tz = tz

    def slavtime(self):    
        os.environ['TZ'] = self.tz
        time.tzset()
        return time.strftime('%X %x %Z')




