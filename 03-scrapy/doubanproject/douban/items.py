# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
        title = scrapy.Field()
        scriptwriter = scrapy.Field()
        roles = scrapy.Field()
        # film_type = scrapy.Field()
        poster_url = scrapy.Field()
        # poster_img = scrapy.Field()
        # detail = scrapy.Field()
