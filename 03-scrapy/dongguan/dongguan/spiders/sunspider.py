# -*- coding:utf-8 -*-
import scrapy
import re

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from dongguan.items import DongguanItem

class DongGuanSpider(CrawlSpider):
        name = 'dongguan'
        allow_domains = ['wz.sun0769.com']
        start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

        rules = (
                # Rule(LinkExtractor(allow=r'type=4&page=\d+')),
                Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'),callback='parse_item'),
        )

        def parse_item(self, response):
                # 提问：梁屋山边路与梁屋北路违停严重  编号:194771
                item = DongguanItem()
                re_title =  Selector(response=response).xpath("/html/body/div[6]/div/div[1]/div[1]/strong/text()").extract()[0]
                # title =re.match(r'提问：(\S+) +编号：(\d+)',re_title).group(1)
                title = re_title.decode().encode('utf-8').split(" ")[0].split('：')[-1]
                # number =re.match(r'提问：(\S+) +编号：(\d+)',re_title).group(2)
                number = re_title.decode().encode('utf-8').split(" ")[-1].split('：')[-1]
                content = Selector(response=response).xpath("//html/body/div[6]/div/div[2]/div[1]/text()").extract()
                # re_date_time=Selector(response=response).xpath("//p[@class='te12h']/text()").extract()
                # data_time = re.match(r'\S+ 发言时间：(\w \w)',re_date_time).group(1)
                # date_time = re_date_time.split(' ')[1].split('：')[-1]
                status = Selector(response=response).xpath("//div[@class='audit']/div[@class='cleft']/span/text()").extract()

                item['title'] = title
                item['number'] = number
                item['content'] = content[0]
                # item['date_time'] = date_time
                item['status'] = status[0]

                print '\n',re_title,'\n'
                

                yield item
                










