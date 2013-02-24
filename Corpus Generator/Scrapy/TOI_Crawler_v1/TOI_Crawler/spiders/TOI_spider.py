#
#   Created By Anirban Das
#   Date - 16 January 2013
#
#
#   This is the spider that will crawl any seed page given as input
#
#   name of the spider is Toi
#  
#    To run the spider
#   type $ scrapy crawl Toi
#   
#  make sure you are in the scrapy directory otherwise you will not be
#   to crawl
#
#






from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from TOI_Crawler.items import ToiCrawlerItem
from scrapy.exceptions import CloseSpider
import os

class ToiCrawlerSpider(BaseSpider):

    name = "Toi"
    allowed_domains = ["timesofindia.indiatimes.com"]
    os.system('clear')
    print "Enter URL of a seed page (page of an article, not a topic):",
    seed = raw_input()
    start_urls = [seed]
    idx1 = seed.find('.com/') + 5
    idx2 = seed.find('/', idx1 + 1)
    idx2 = seed.find('/', idx2 + 1)
    sp_category = seed[idx1:idx2]
    links_with_error = []
    close_down = False
    
    def parse(self, response):
        
        if self.close_down:
            raise CloseSpider('Done')
        
        w = ToiCrawlerItem()
        currentURL = response.url
        if currentURL.find('/articleshow/') != -1:
            hxs = HtmlXPathSelector(response)
            title = hxs.select('//title/text()').extract()
            w['title'] = title
            content = hxs.select('//tmp//text()').extract()
            content =  ''.join(content)
            if content.find('a') == -1:
                 con = hxs.select('//div[contains(@class,"Normal")]')
                 if len(con) > 1:
                     self.links_with_error.append(currentURL)
                 else:
                     content = con.select('text()').extract()
                     w['content'] = content
                     w['url'] = currentURL
                     yield w
            else:
                 w['content'] = content
                 w['url'] = currentURL
                 yield w
        
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//a[contains(@href,"/%s")]/@href' % self.sp_category).extract()
        
        for site in sites:
            site = str(site)
            idx = site.rfind('?')
            if idx != -1:
                site = site[:idx]
            if site.find('/videos/') == -1:
                 if site.find('http://')==-1:
                    site = "http://timesofindia.indiatimes.com" + site
                    # May help to debug: print site
                    yield Request(site, callback=self.parse)
                 else:
                    yield Request(site, callback=self.parse)
