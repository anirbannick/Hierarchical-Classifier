'''
Created on Feb 21, 2013

@author: ayush
'''

from date_generator import Date

class URL_gen():
    
    def __init__(self, sday, smon, syr, eday, emon, eyr, num):
        self.date = Date(sday, smon, syr, eday, emon, eyr)
        self.num = num
        self.current = self.date.next()
        
    def fetch(self):
        if not self.current is None:
            link = "http://timesofindia.indiatimes.com/" + str(self.current['year']) + "/" + str(self.current['month']) + "/" + str(self.current['day'])
            link = link + "/archivelist/year-" + str(self.current['year']) + ",month-" + str(self.current['month']) + ",starttime-" + str(self.num) + ".cms"
            self.num = self.num + 1
            self.current = self.date.next()
            return link
        else:
            return None

    def fetch_all(self):
        ls = []
        x = self.fetch()
        while not x is None:
            ls.append(x)
            x = self.fetch()
        return ls