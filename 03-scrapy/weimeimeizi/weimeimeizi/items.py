# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeimeimeiziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
        title = scrapy.Field()
        tag = scrapy.Field()
        img_urls = scrapy.Field()
        imgs_paths = scrapy.Field()
        # img_urls = scrapy.Field()
