'''
Created on Feb 21, 2013

@author: ayush
'''

from datetime import date
from dateutil.rrule import rrule, DAILY

class Date():
    
    def __init__(self, sday, smon, syr, eday, emon, eyr):
        self.start_date = date(syr, smon, sday)
        self.end_date = date(eyr, emon, eday)
        self.dates = [dt for dt in rrule(DAILY, dtstart=self.start_date, until=self.end_date)]
        self.idx = 0
        self.max = len(self.dates)
    
    def next(self):
        if self.idx < self.max:
            self.idx = self.idx + 1
            x = self.dates[self.idx - 1]
            dict = {'day' : x.day, 'month' : x.month, 'year': x.year}
            return dict
        else:
            return None
