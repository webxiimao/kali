# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BuildingItem(scrapy.Item):
        address = scrapy.Field()
        average_price = scrapy.Field()
        average_price_unit = scrapy.Field()
        city_id = scrapy.Field()
        city_name = scrapy.Field()
        district_id = scrapy.Field()
        district_name = scrapy.Field()
        house_type = scrapy.Field()
        resblock_name = scrapy.Field()
        max_area = scrapy.Field()
        min_area = scrapy.Field()
        create_time = scrapy.Field()
        open_time = scrapy.Field()
        status = scrapy.Field()
        total_price_start = scrapy.Field()
        total_price_start_unit = scrapy.Field()
        isDelete = scrapy.Field()
        county_id = scrapy.Field()
        county_name = scrapy.Field()
        cover_pic = scrapy.Field()
        url = scrapy.Field()
        tags = scrapy.Field()



class BuildingTagsItem(scrapy.Item):
        building_id = scrapy.Field()
        tag_id = scrapy.Field()


class CityItem(scrapy.Item):
        name = scrapy.Field()


class DistrictItem(scrapy.Item):
        name = scrapy.Field()


class CountyItem(scrapy.Item):
        name = scrapy.Field()


class ProjectTagsItem(scrapy.Item):
        tags = scrapy.Field()