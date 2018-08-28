# -*- coding:utf-8 -*-
import scrapy
import json
import sys
from scrapy.selector import Selector

from scrapy.http import Request

from meirenku.items import MeirenkuItem

reload(sys)
sys.setdefaultencoding('utf8')

class Meirenku(scrapy.Spider):
        name = 'meirenku'
        current_id = '19768826'
        start_urls = ['http://huaban.com/boards/favorite/beauty']
        base_url = 'http://huaban.com/boards/favorite/beauty?jlc67zvd&max='
        count = 1
        count_pin = 1
        
                
        def parse(self, response):
  
              
                text = json.loads(response.body)
                if self.count >= 30 or not text['boards'] :
                        return 
                self.current_id = text['boards'][-1]['board_id']
                self.count += 1
                for board in text['boards']:
                        self.board_id = str(board['board_id'])
                        yield Request('http://huaban.com/boards/%s/'%(self.board_id), callback=self.parse_next)
                yield Request('%s%s&limit=10&wfl=1'%(self.base_url,self.current_id),callback=self.parse)

        def parse_next(self,response):
                #?jld2d7ku&max=418500334&limit=20&wfl=1
                data = json.loads(response.body)
                img_urls = []
                item = MeirenkuItem()
                if len(data['board']['pins']) <= 0 or not data['board']:
                        return
                for pin in data['board']['pins']:
                        #http://img.hb.aicdn.com/22066df2cd7e0ef13fd030fff47a71a84a69bda2ada60-B58rsf_fw658
                        img_url = "http://img.hb.aicdn.com/"+str(pin['file']['key'] )
                        # print "http://img.hb.aicdn.com/"+str(pin['file']['key'] )
                        img_urls.append(img_url)

                item['img_urls'] = img_urls
                yield item
                yield Request('http://huaban.com/boards/%s/?jld2d7ku&max=%s&limit=20&wfl=1'%(self.board_id,str(data['board']['pins'][-1]['pin_id'])),callback=self.parse_next)

                