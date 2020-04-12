import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class GenSpiderCrawl(CrawlSpider):
    name = 'un_programme_crawler'
    allowed_domains = ['un.org']
    start_urls = ['http://www.un.org/en/sections/about-un/' \
                  'funds-programmes-specialized-agencies-and-others/index.html']
    rules = (Rule(LinkExtractor(
        allow=('funds-programmes-specialized-agencies-and-others'),
        deny=('zh/sections', 'ru/sections', 'fr/sections'))
                  , callback='parse_page'),)

    def parse_page(self, response):
        # Extract the list of agencies using the specified selector
        list_of_agencies = response.css('div.field-item.even > h4::text').extract()

        # Write out the list of agencies extracted to a file
        for agency in list_of_agencies:
            with open('un_agencies.txt', 'a+') as f:
                f.write(agency + '\n')
