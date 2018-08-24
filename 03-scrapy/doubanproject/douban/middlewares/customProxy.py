#-*- coding:utf-8 -*-
from douban.middlewares.resource import PROXY_LIST
import random



class RandomProxy(object):
        def process_request(self, request, spider):
                proxy = random.choice(PROXY_LIST)
                print '\n',proxy,'代理\n'
                request.meta['proxy'] = 'http://%s'%proxy
