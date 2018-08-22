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
                item = DoubanItem()
                title = Selector(response=response).xpath('//h1/span[1]/text()').extract()
                scriptwriter = Selector(response=response).xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
                roles = Selector(response=response).xpath('//*[@id="info"]/span[3]/span[2]/*/a/text()').extract()
                film_types = Selector(response=response).xpath("//*[@id='info']/span[@property='v:genre']/text()").extract()
                poster_url = Selector(response=response).xpath('//*[@id="mainpic"]/a/img/@src').extract()

                print '\n'+title[0]+'\n'
                item['title'] = title[0]
                item['scriptwriter'] = scriptwriter[0]
                for role in roles:
                        item['roles'] += role + '/'
                # for _type in film_types:
                #         item['film_type'] += _type + '/'
                item['poster_url'] = poster_url[0]

                yield item

                # for title in titles:
        