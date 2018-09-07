# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from lianjia import settings
# from scrapy import log

from lianjia.items import BuildingItem, BuildingTagsItem, CityItem, DistrictItem, CountyItem, ProjectTagsItem

class LianjiaPipeline(object):
        def __init__(self):
                self.connect = pymysql.connect(
                        host=settings.MYSQL_HOST,
                        db=settings.MYSQL_DBNAME,
                        user=settings.MYSQL_USER,
                        passwd=settings.MYSQL_PASSWD,
                        charset='utf8',
                        use_unicode=True)
                self.cursor = self.connect.cursor()

        def process_item(self, item, spider):

                if item.__class__ == BuildingItem:
                        '''
                        处理地区
                        '''

                        self.cursor.execute(
                                "SELECT * FROM city where name=%s",(item['city_name'].encode('utf-8'))
                        )
                        city = self.cursor.fetchone()
                        if city:
                                print 'this record city has been in mysql'
                        else:
                                self.cursor.execute(
                                        "insert into city(name) values(%s)",(item['city_name'].encode('utf-8'))
                                )
                                
                                self.connect.commit()


                        self.cursor.execute(
                                "SELECT * FROM district where name=%s",(item['district_name'].encode('utf-8'))
                        )
                        
                        district = self.cursor.fetchone()
                        if district:
                                print 'this record district has been in mysql'
                        else:
                                self.cursor.execute(
                                        "insert into district(name ,city_id) values(%s,(select id from city where name =%s))",(item['district_name'].encode('utf-8'),item['city_name'].encode('utf-8'))
                                )
                                
                                
                                self.connect.commit()
                        
                        self.cursor.execute(
                                "SELECT * FROM county where name=%s",(item['county_name'].encode('utf-8'))
                        )
                        
                        county = self.cursor.fetchone()
                        if county:
                                print 'this record county has been in mysql'
                        else:
                                self.cursor.execute(
                                        "insert into county(name ,district_id) values(%s,(select id from district where name =%s))",(item['county_name'].encode('utf-8'),item['district_name'].encode('utf-8'))
                                )
                                
                                
                                self.connect.commit()
                        '''
                        处理building记录
                        '''

                        self.cursor.execute(
                                "SELECT * FROM building where resblock_name=%s",(item['resblock_name'].encode('utf-8'))
                        )

                        build = self.cursor.fetchone()

                        if build:
                                print "this build has been in sql"
                        else:
                                self.cursor.execute(
                                        "insert into building(address, average_price, average_price_unit, city_id, district_id, house_type, resblock_name, max_area, min_area, open_time, status, total_price_start, total_price_start_unit, county_id, cover_pic,url) values(%s,%s,%s,(select id from city where name= %s),(select id from district where name= %s),%s,%s,%s,%s,%s,%s,%s,%s,(select id from county where name= %s),%s,%s)",(item['address'].encode('utf-8'),item['average_price'],item['average_price_unit'].encode('utf-8'),item['city_name'].encode('utf-8'),item['district_name'].encode('utf-8'),item['house_type'].encode('utf-8'),item['resblock_name'].encode('utf-8'),item['max_area'],item['min_area'],item['open_time'],item['status'],item['total_price_start'],item['total_price_start_unit'].encode('utf-8'),item['county_name'].encode('utf-8'),item['cover_pic'].encode('utf-8'),item['url'])
                                )
                                

                                self.connect.commit()

                # if item.__class__ == ProjectTagsItem:
                        '''
                        处理tags
                        '''
                        for tag in item['tags']:
                                # print tag
                                self.cursor.execute(
                                        "select id from project_tags where tag=%s",(tag.encode('utf-8'),)
                                )
                                ret = self.cursor.fetchone()
                                if ret:
                                        pass
                                else:
                                
                                        self.cursor.execute(
                                                "insert into project_tags(tag) values( %s)",(tag.encode('utf-8'),)
                                        )
                
                                self.cursor.execute(
                                        "insert into building_tags(tag_id,building_id) values((select id from  project_tags where tag= %s), (select id from building where resblock_name=%s))",(tag.encode('utf-8'),item['resblock_name'].encode('utf-8'))
                                )

                                self.connect.commit()
                                          


                        

                        

          




                        

