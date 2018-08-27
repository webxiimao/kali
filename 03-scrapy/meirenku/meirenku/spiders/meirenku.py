# -*- coding:utf-8 -*-
import scrapy
import json
import sys
from scrapy.selector import Selector

from scrapy.http import Request

reload(sys)
sys.setdefaultencoding('utf8')

class Meirenku(scrapy.Spider):
        name = 'meirenku'
        start_urls = ['http://huaban.com/boards/favorite/beauty/?jlc2lzkm&max=10000&limit=20&wfl=1']

        def parse(self, response):
                print '\n'
                print json.loads(response.body)
                print '\n'
                text = response.body
                # text = json.dumps(json.loads(response.body))
                # text = json.dumps(dict(response.body), ensure_ascii = False) + ",\n"
                f = open('meizijson.json', 'w')
                f.write(text.encode('utf-8'))
                f.close()
                