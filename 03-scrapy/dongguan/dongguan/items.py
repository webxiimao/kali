# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
        title = scrapy.Field()
        number = scrapy.Field()
        content = scrapy.Field()
        date_time = scrapy.Field()
        status = scrapy.Field()

