# Scrapy settings for TOI_Crawler_v2 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'TOI_Crawler_v2'

SPIDER_MODULES = ['TOI_Crawler_v2.spiders']
NEWSPIDER_MODULE = 'TOI_Crawler_v2.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'TOI_Crawler_v2 (+http://www.yourdomain.com)'


DEFAULT_ITEM_CLASS = 'TOI_Crawler_v2.items.ToiCrawlerV2Item'

ITEM_PIPELINES = ['TOI_Crawler_v2.pipelines.ToiCrawlerV2Pipeline']
DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'

LOG_LEVEL = 'INFO'

