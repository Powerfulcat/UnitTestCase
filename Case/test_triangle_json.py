import unittest
from Func.triangle import Triangle
from ReadData.read_json import ReadJson

triangle_class = Triangle()
readJson_class = ReadJson()


class TestTriangleJson(unittest.TestCase):
    def test_triangleJson(self):
        for i in range(len(readJson_class.readJson())):
            result = triangle_class.func_triangle(int(readJson_class.readJson()[i]['side1']),
                                                  int(readJson_class.readJson()[i]['side2']),
                                                  int(readJson_class.readJson()[i]['side3']))
            # 设置断言
            self.assertEqual(result, readJson_class.readJson()[i]['expect'])
    
            # 设置打印
            print(result)
            print(int(readJson_class.readJson()[i]['side1']),
                  int(readJson_class.readJson()[i]['side2']),
                  int(readJson_class.readJson()[i]['side3']),
                  readJson_class.readJson()[i]['expect'], '>>>>>验证成功!')


if __name__ == '__main__':
    unittest.main()
