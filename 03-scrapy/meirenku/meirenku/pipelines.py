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

class MeirenkuPipeline(ImagesPipeline):
        IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
        def get_media_requests(self, item, info):
                default_headers = {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8,zh-TW;q=0.7",
                        "Cache-Control": "no-cache",
                        "Connection": "keep-alive",
                        "Host": "img.hb.aicdn.com",
                        "Pragma": "no-cache",
                        "Upgrade-Insecure-Requests": "1",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                }
                img_urls = item['img_urls']
                for img_url in img_urls:
                        yield scrapy.Request(img_url,headers=default_headers)
       


        def item_completed(self, result, item, info):
                image_paths = [x['path'] for ok, x in result if ok]
                if not image_paths:
                        raise DropItem("Item contains no images")
                item['imgs_paths'] = image_paths
                return item
