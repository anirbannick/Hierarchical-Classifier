# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from TOI_Crawler_v2.path_fixer import fix_path
import os
import categories
import json

class ToiCrawlerV2Pipeline(object):

    def __init__(self):
        self.j = 0
        self.start = 1
        print "\nEnter ABSOLUTE path of top directory of Corpus:",
        self.path = raw_input()
        if self.path[-1] == '/':
            self.path = self.path[:-1]
        
        self.limit = int(raw_input("Enter limit: "))
        categories.init()
        for i in categories.category:
            complete_path = self.path + '/' + i
            fix_path(complete_path)
        print        
    
    def process_item(self, item, spider):
        if len(categories.category) == 0  and not spider.close_down:
            print "\n\nTask Successfully completed!\n"
            spider.close_down = True
        else:
            item_dict = dict(item)
            url = item_dict['url']
            for i in categories.category:
                if self.j <= self.limit:
                    if url.find(i) != -1:
                        self.category = i
                        categories.category[i] = categories.category[i] + 1
                        self.j = categories.category[i]
                        file = open('%s/%s/%s.jl' % (self.path, self.category, self.j), 'wb')
                        line = json.dumps(item_dict) + "\n"
                        if self.start == 1:
                            print "\n\nSaved data:\n"
                            self.start = 2
                        print str(self.j) + '\t' + item_dict['title'][0]
                        file.write(line)
                        break
                else:
                    categories.category.pop(i)                    
        return item
