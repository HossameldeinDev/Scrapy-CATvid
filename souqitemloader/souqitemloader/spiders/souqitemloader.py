import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from souqitemloader.items import SouqItem

class ProductDetails(scrapy.Spider):
    name = 'macbook_scraper_itemloader'

    start_urls = ['https://egypt.souq.com/eg-en/macbook/s/?as=1']

    def parse(self, response):
        search_results = response.css('.tpl-append-results>div')

        for product in search_results:

            product_loader = ItemLoader(item=SouqItem(), selector=product)
            product_loader.default_output_processor = TakeFirst()
            product_loader.add_css('title', '.itemTitle::text')
            product_loader.add_css('link', '.item-content> .itemLink::attr(href)')
            product_loader.add_css('price', '.itemPrice::text')

            yield product_loader.load_item()


