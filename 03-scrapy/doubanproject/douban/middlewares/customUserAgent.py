from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from douban.middlewares.resource import USER_AGENT_LIST

import random

class RandomUserAgent(UserAgentMiddleware):
        def process_request(self, request, spider):
                ua = random.choice(USER_AGENT_LIST)

                print ua, '\n-----------------yyyyyyyyyyyyyyyyyyyyyyyyy\n'
                request.headers.setdefault('User-Agent', ua)    