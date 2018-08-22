from douban.items import DoubanItem


class DoubanPipeline(object):
        # __init__方法是可选的，做为类的初始化方法
        def __init__(self):
                # 创建了一个文件
                self.filename = open("dianying.json", "w")

        # process_item方法是必须写的，用来处理item数据
        def process_item(self, item, spider):
                jsontext = json.dumps(dict(item), ensure_ascii = False) + "\n"
                self.filename.write(jsontext.encode("utf-8"))
                return item

        # close_spider方法是可选的，结束时调用这个方法
        def close_spider(self, spider):
                self.filename.close()