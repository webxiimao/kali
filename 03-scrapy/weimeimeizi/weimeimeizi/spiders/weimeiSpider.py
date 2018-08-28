# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class weimeiSpider(scrapy.Spider):
        name = "weimei"
        allow_domains = ['http://www.mmonly.cc/']
        start_urls = ['http://www.mmonly.cc/tag/']

        def parse(self, response):
                tag_as = Selector(response=response).xpath(u'//h2[text()="美女特征"]/following-sibling::div[1][@class="TagList"]/a/@href').extract()
                for tag_a in tag_as:
                        print '\n',tag_a,'\n'
                        yield Request('%s%s'%(self.start_urls, tag_a), callback=self.parse_items)


        def parse_items(self, response):
                item_urls = Selector(response=response).xpath("//div[@class='item_t']//div[@class='ABox']/a/@href").extract()
                for item_url in item_urls:
                        yield Request(item_url, callback=self.parse_imgs)


        def parse_imgs(self, response):
                pass