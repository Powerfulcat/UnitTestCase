import unittest
# 导入三角形类
from Func.triangle import Triangle
# 导入xml数据解析类
from ReadData.read_xml import ReadXml

triangle_class = Triangle()
readXml_class = ReadXml()


class TestTriangleXml(unittest.TestCase):
    def test_triangle_xml(self):
        for i in range(readXml_class.getLen('side')):
            result = triangle_class.func_triangle(int(readXml_class.readxml('side', i, 'side1')),
                                                  int(readXml_class.readxml('side', i, 'side2')),
                                                  int(readXml_class.readxml('side', i, 'side3')))
            # 设置断言
            self.assertEqual(result, readXml_class.readxml('side', i, 'expect'))

            # 只为调试代码是查看运行结果,核对代码执行过程,实际工作不需要书写这部分代码
            print('三角形函数返回的结果:', result)
            print(int(readXml_class.readxml('side', i, 'side1')),
                  int(readXml_class.readxml('side', i, 'side2')),
                  int(readXml_class.readxml('side', i, 'side3')),
                  readXml_class.readxml('side', i, 'expect'), '>>>>>>验证成功!')


if __name__ == '__main__':
    unittest.main()
