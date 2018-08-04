# 1.导包
from xml.dom import minidom


class ReadXml(object):
    def readxml(self, node, num, childNode):
        # 2.获取文件
        dom = minidom.parse('./DataPool/triangle.xml')
        # 3.获取文件全部元素
        root = dom.documentElement
        # print(root)
        # 4.获取子标签内容
        # elements = root.getElementsByTagName('side')
        # print(elements)
        element = root.getElementsByTagName(node)[int(num)]
        # print(element)
        # 5.获取下一层子标签内容
        child_element = element.getElementsByTagName(childNode)[0].firstChild.data
        return child_element

    def getLen(self, node):
        dom = minidom.parse('./DataPool/triangle.xml')
        root = dom.documentElement
        element = root.getElementsByTagName(node)
        return len(element)


if __name__ == '__main__':
    print(ReadXml().readxml('side', 1, 'side1'))
    print(type(ReadXml().readxml('side', 1, 'side1')))
    print(ReadXml().getLen('side'))
