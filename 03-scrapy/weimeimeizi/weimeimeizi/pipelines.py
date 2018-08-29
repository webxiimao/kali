# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import os
import time

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

class WeimeimeiziPipeline(ImagesPipeline):
        default_headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Host": "t1.hxzdhn.com",
                'Referer':'http://www.mmonly.cc/tag/',
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        }
        def get_media_requests(self, item, info):
                urls = item['img_urls']
                print 'is download' + urls[0]
                # print '\n',url,'\n'
                for url in urls:
                        yield scrapy.Request(url, meta={'item': item},headers=self.default_headers)

        def item_completed(self, result, item, info):
                image_paths = [x['path'] for ok, x in result if ok]
                if not image_paths:
                        raise DropItem("Item contains no images")
                item['imgs_paths'] = image_paths
                return item

        def file_path(self, request, response=None, info=None):#自定义存储路径
                item = request.meta['item']  # 通过上面的meta传递过来item
                # print item['img_urls']
                title = item['title']
                path = item['tag']
                # image_guid = request.url.split('/')[-1]
                filename = u'full/%s/%s.jpg'%(path, title)#title为二级目录
                return filename
