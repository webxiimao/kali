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
        current_id = '19768826'
        start_urls = ['http://huaban.com/boards/favorite/beauty?jlc67zvd&max=19768826&limit=10&wfl=1']
        base_url = 'http://huaban.com/boards/favorite/beauty?jlc67zvd&max='
        count = 1
        

        # def start_requests(self):
                


        def parse(self, response):
                print '\n'
                print json.loads(response.body)
                print '\n'
                text = json.loads(response.body)
                self.current_id = text['boards'][-1]['board_id']
                self.count += 1
                # text = json.dumps(json.loads(response.body))
                # text = json.dumps(dict(response.body), ensure_ascii = False) + ",\n"
                f = open('meizijson%s.json'%(self.count), 'w')
                f.write(response.body.encode('utf-8'))
                f.close()
                yield Request('%s%s&limit=10&wfl=1'%(self.base_url,self.current_id),callback=self.parse)

        # def parse_next(self,response):
        #         f = open('meizijson%s.json'%(self.count), 'w')
        #         f.write(response.body.encode('utf-8'))
        #         f.close()
                