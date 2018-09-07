# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
import json
# from scrapy import log


import sys
reload(sys)
sys.setdefaultencoding('utf8')

from lianjia.items import BuildingItem, BuildingTagsItem, CityItem, DistrictItem, CountyItem, ProjectTagsItem


class LianjiaSpider(scrapy.Spider):
        name = 'lianjia'
        allow_domains = ['https://sz.fang.lianjia.com/']
        base_url= 'https://sz.fang.lianjia.com/loupan/'
        start_urls = []


        def __init__(self):
                for page in range(1, 101):
                        url = "%spg%s/?_t=1"%(self.base_url, page)
                        self.start_urls.append(url)
                # self.start_urls.append("%spg1/?_t=1"%(self.base_url))


        def parse(self, response):
                rep = json.loads(response.body)
                # f = open('lianjialist.json', 'w')
                # f.write(json.dumps(rep['data']['list'] ,ensure_ascii = False).encode('utf-8'))
                # f.close()
                buildings = rep['data']['list']
                # print json.loads(json.dumps(buildings,ensure_ascii=False, encoding='utf-8'))
                
                
                for building in buildings:
                        
                        build_item = BuildingItem()

                        build_item['address'] = building['address']
                        build_item['average_price'] = building['average_price']
                        build_item['average_price_unit'] = building['avg_price_start_unit']

                        build_item['city_name'] = building['city_name']
                        build_item['district_name'] = building['district_name']

                        build_item['house_type'] = building['house_type']
                        build_item['resblock_name'] = building['resblock_name']
                        build_item['max_area'] = building['max_frame_area']
                        build_item['min_area'] = building['min_frame_area']
                        build_item['open_time'] = building['open_date']
                        build_item['status'] = building['sale_status']
                        build_item['total_price_start'] = building['total_price_start']
                        build_item['total_price_start_unit'] = building['total_price_start_unit']

                        build_item['county_name'] = building['bizcircle_name']

                        build_item['cover_pic'] = building['cover_pic']
                        build_item['url'] = building['url']


                        

                        build_item['tags'] = []

                        for tag in building['project_tags']:
                                build_item['tags'].append(tag['desc'])

                        yield build_item
                        # yield project_tag_item




                        
                        