# 不用导包

class ReadTxt(object):
    def readTxt(self):
        # 打开文件
        with open('./DataPool/triangle.txt', 'r', encoding='utf-8') as f:
            """
            readlines():读取多行数据
            readline():读取单行数据
            read():读取数据,获取大量内容的文件时,一般需要制定文件大小.
            """
            data = f.readlines()
            # print(data)
            """
            strip():去除换行符号,空格,制表符
            split():使用传入的内容分隔数据,并返回列表型数据
            """
            # 声明空列表
            data_list = []
            # 遍历
            for i in data:
                # print(i.strip().split(','))
                data_list.append(i.strip().split(','))
            return data_list


if __name__ == '__main__':
    print(ReadTxt().readTxt())
