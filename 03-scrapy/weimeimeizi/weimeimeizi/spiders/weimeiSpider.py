# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from weimeimeizi.items import WeimeimeiziItem
import re

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class weimeiSpider(scrapy.Spider):
        name = "weimei"
        allow_domains = ['http://www.mmonly.cc/']
        start_urls = ['http://www.mmonly.cc/tag/']

        def parse(self, response):
                tag_as = Selector(response=response).xpath(u'//h2[text()="美女特征"]/following-sibling::div[1][@class="TagList"]/a')
                base_url = self.allow_domains[0][0:-1]
                
                for tag_a in tag_as:
                        item = {}
                        item['tag'] = tag_a.xpath(".//text()").extract()[0]
                        url = tag_a.xpath(".//@href").extract()[0]
                        # print '\n',url,'\n'
                        yield Request('%s%s'%(base_url, url), callback=self.parse_items, meta={'item':item})


        def parse_items(self, response):
                item = response.meta['item']
                item_urls = Selector(response=response).xpath("//div[@class='item_t']//div[@class='ABox']/a/@href").extract()
                for item_url in item_urls:
                        # self.meta['url'] = item_url
                        yield Request(item_url, callback=self.parse_imgList, meta={'item':item,'url':item_url})
                # yield Request(item_urls[0], callback=self.parse_imgList, meta={'item':item,'url':item_urls[0]})


        def parse_imgList(self, response):
                # print response.body
                item = response.meta['item']
                max_li = Selector(response=response).xpath("//span[@class='totalpage']/text()").extract()
                if len(max_li) <= 0:
                        return
                # print '\n',,'\n'
                b_url = response.meta['url']
                yield Request(b_url, callback=self.parse_imgs, meta={'item':item})
                for i in range(2, int(max_li[0]) + 1):
                        all_url = b_url[0:-5]+'_'+ str(i)+'.html'
                        print '\n',all_url,'\n'

                        
                        yield Request(all_url, callback=self.parse_imgs, meta={'item':item})
                # yield Request(b_url[0:-5]+'_2'+ '.html', callback=self.parse_imgs, meta={'item':item})


        def parse_imgs(self, response):

                get_item = response.meta['item']
                item = WeimeimeiziItem()
                
                img_src = Selector(response=response).xpath("//div[@id='big-pic']//img/@src").extract()
                title = Selector(response=response).xpath("//h1/text()").extract()[0]
                page = Selector(response=response).xpath("//h1/span/span[@class='nowpage']/text()").extract()[0]
                # print 'is handling' + img_src[0]
                # item['tag'] = response.meta['tag']
                item['tag'] = get_item['tag']
                item['img_urls'] = img_src
                item['title'] = title + page
                yield item
                
                