import scrapy
from souq.items import SouqItem



class ProductDetails(scrapy.Spider):
    name = 'macbook_scraper'

    start_urls = ['https://egypt.souq.com/eg-en/macbook/s/?as=1']

    def parse(self, response):
        search_results = response.css('.tpl-append-results>div')

        for product in search_results:

            productItem = SouqItem()

            productItem['title'] = search_results.css('.itemTitle').xpath('normalize-space()').extract_first()
            productItem['link'] = search_results.css('.item-content> .itemLink::attr(href)').extract_first()
            productItem['price'] = search_results.css('.itemPrice::text').re(r'[\d.,]+')[0]

            yield productItem