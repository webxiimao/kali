# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
import os


class doubanSpider(scrapy.Spider):
        #target https://www.douban.com/people/158983390/
        name = 'douban'
        start_urls = ['https://www.douban.com/accounts/login']
        allow_domains = ['https://www.douban.com/']

        def parse(self,response):
                # self.login_url = "https://accounts.douban.com/login"
                self.login_response = response
                self.captcha_id = Selector(response=response).xpath("//input[@name='captcha-id']/@value").extract()[0]
                captcha_img = Selector(response=response).xpath("//img[@id='captcha_image']/@src").extract()
                if len(captcha_img) > 0:
                        print '有验证码登录...',captcha_img[0]
                        yield Request(captcha_img[0], callback=self.handle_captcha_by_self)
                       
                else:
                        print '无验证码登录'

                
                


        def handle_captcha_by_self(self, response):
                if os.path.exists('captcha.jpg'):
                        os.remove('captcha.jpg')
                f = open('captcha.jpg', 'ab')
                f.write(response.body)
                f.close()

                captcha = raw_input('请输入刚刚保存的验证码')

                # captcha-solution
                data = {
                        'redir':'https://www.douban.com/people/158983390/',
                        'form_email':'339290504@qq.com',
                        'form_password':'myy436627',
                        'captcha-solution':captcha,
                        'captcha-id':self.captcha_id,
                        'login':'登录'
                }

                yield scrapy.FormRequest.from_response(
                        # login_url,
                        self.login_response,
                        formdata = data,
                        callback=self.parse_items
                )

        def parse_items(self,response):
                # print response
                f = open('mydouban.html' , 'w')
                f.write(response.body)
                f.close()
                

                