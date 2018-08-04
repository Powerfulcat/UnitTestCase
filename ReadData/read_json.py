# 导包
import json


class ReadJson(object):
    def readJson(self):
        # 打开文件
        with open('./DataPool/triangle.json', 'r', encoding='utf-8') as f:
            # 加载json文件的方法
            source = json.load(f)
            # print(source)
            # 根据键名(key)取出大列表数据
            source_data = source['data']
            return source_data


if __name__ == '__main__':
    print(ReadJson().readJson())
