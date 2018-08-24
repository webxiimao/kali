import scrapy
import re
from douban.items import DoubanItem
from scrapy.http import Request
from scrapy.selector import Selector

class doubanSpider(scrapy.Spider):
        name = "douban"
        allow_domains = ['https://movie.douban.com/']
        basic_urls = 'https://movie.douban.com/top250?'
        # start_urls = ['https://movie.douban.com/top250?start=0&filter=']
        start_urls = []
        # def parse(self, response):
        #         for page in range(0,10):
        #                 full_url = self.start_url

        def __init__(self):
                for page in range(0,10):
                        full_url = self.basic_urls+'start='+str(page*25)+'&filter='
                        print full_url
                        self.start_urls.append(full_url)

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
                roles = Selector(response=response).xpath('//span[@class="attrs"]//a[starts-with(@rel,"v:starring")]/text()').extract()
                film_types = Selector(response=response).xpath("//*[@id='info']/span[@property='v:genre']/text()").extract()
                poster_url = Selector(response=response).xpath('//*[@id="mainpic"]/a/img/@src').extract()

                # print '\n'+film_types[0]+'\n'
                item['title'] = title[0]
                item['scriptwriter'] = scriptwriter[0]
                print '\n======================roles===============\n'
                # role_list = []
                # for role in roles:
                #         rolename = role.xpath('./a/text()').extract()
                #         print '\n',rolename,'\n'
                #         role_list.append(rolename)
                # # item['roles'] = roles
                item['roles'] = '/'.join(roles)
               
                print '\n======================roles===============\n'
                item['film_type'] = '/'.join(film_types)
                item['poster_url'] = poster_url[0]

                yield item

                # for title in titles:
        