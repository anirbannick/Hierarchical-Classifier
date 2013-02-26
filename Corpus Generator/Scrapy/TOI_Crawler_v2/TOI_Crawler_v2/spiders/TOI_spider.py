from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from TOI_Crawler_v2.items import ToiCrawlerV2Item
from TOI_Crawler_v2.url_generator import URL_gen 
from scrapy.exceptions import CloseSpider
from .. import categories
import os

class ToiCrawlerV2Spider(BaseSpider):
    name = "Toi"
    allowed_domains = ["timesofindia.indiatimes.com"]
    os.system('clear')
    sday = input("Enter starting date: ")
    smon = input("Enter starting month: ")
    syr  = input("Enter starting year: ") 
    eday = input("Enter end date: ")
    emon = input("Enter end month: ")
    eyr  = input("Enter end year: ")
    num  = input("Enter starttime number: ")
    urlobj = URL_gen(sday, smon , syr, eday, emon, eyr, num)

    start_urls = []
    start_urls = urlobj.fetch_all()
    
    links_with_error = []
    close_down = False
    
    def parse(self, response):
        
        if self.close_down:
            raise CloseSpider('Done')
        
        w = ToiCrawlerV2Item()
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
        
        else:   
            hxs = HtmlXPathSelector(response)
            sites = hxs.select('//a[contains(@href,"articleshow")]/@href').extract()
            
            for site in sites:
                site = str(site)
                idx = site.rfind('?')
                if idx != -1:
                    site = site[:idx]
                for i in categories.category:
                    if site.find(i) != -1:
                        if site.find('/videos/') == -1:
                             if site.find('http://')==-1:
                                site = "http://timesofindia.indiatimes.com" + site
                                # May help to debug: print site
                                yield Request(site, callback=self.parse)
                             else:
                                yield Request(site, callback=self.parse)
