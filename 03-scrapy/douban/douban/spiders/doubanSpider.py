import scrapy
import re
from douban.items import DoubanItem
from scrapy.http import Request
from scrapy.selector import Selector

class doubanSpider(scrapy.Spider):
        name = "douban"
        allow_domains = ['https://movie.douban.com/']
        start_urls = ['https://movie.douban.com/top250?start=0']

        def parse(self, response):
                # page_urls = response.xpath("//div[@class='hd']/a/@href").extract()
                page_urls = Selector(response=response).xpath("//div[@class='hd']/a/@href").extract()

                for page_url in page_urls:
                        yield Request(page_url, callback=self.details_parse)
                # yield Request(page_urls[0], callback=self.details_parse)


        def details_parse(self, response):
                # titles = response.xpath("//h1/span[1]").extract()
                titles = Selector(response=response).xpath('//h1/span[1]/text()').extract()
                print '\n'+titles[0]+'\n'
                # for title in titles:
