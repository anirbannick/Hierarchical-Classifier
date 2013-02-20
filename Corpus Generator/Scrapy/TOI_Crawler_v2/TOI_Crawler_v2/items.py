# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ToiCrawlerV2Item(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    url = Field()
    content= Field()
    
    def __str__(self):       
        return "ToiCrawlerItem: title=%s url=%s" % (self.get('name'), self.get('url'))

