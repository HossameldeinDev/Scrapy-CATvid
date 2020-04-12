# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
from re import sub
from decimal import Decimal


def convert_price(price):
    if price:
        return float(Decimal(sub(r'[^\d.]', '', price)))


def clean_title(title):
    return ' '.join(title.split())


class SouqItem(scrapy.Item):
    title = scrapy.Field(input_processor=MapCompose(clean_title))
    price = scrapy.Field(input_processor=MapCompose(convert_price))
    link = scrapy.Field()
