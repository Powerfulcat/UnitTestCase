# 导包
import csv


class ReadCsv(object):
    def readCsv(self):
        # 打开文件
        """
        r:读取文件(read)
        encoding='utf-8':指定读取文件的编码格式,防止获取的数据内容乱码!
        """
        with open('./DataPool/triangle.csv', 'r', encoding='utf-8') as f:
            data = csv.reader(f)
            # print(data)
            # 声明空列表
            data_list = []
            # 遍历
            for i in data:
                # print(i)
                data_list.append(i)  # append()列表添加元素的方法
            return data_list


if __name__ == '__main__':
    print(ReadCsv().readCsv())
