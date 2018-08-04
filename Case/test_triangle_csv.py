import unittest
from Func.triangle import Triangle
from ReadData.read_csv import ReadCsv

triangle_class = Triangle()
readCsv_class = ReadCsv()


class TestTriangleCsv(unittest.TestCase):
    def test_trianglecsv(self):
        for i in range(len(readCsv_class.readCsv())):
            result = triangle_class.func_triangle(int(readCsv_class.readCsv()[i][0]),
                                                  int(readCsv_class.readCsv()[i][1]),
                                                  int(readCsv_class.readCsv()[i][2]))
            # 设置断言
            self.assertEqual(result, readCsv_class.readCsv()[i][3])

            # 设置打印,查看效果,实际工作不需要
            print(result)
            print(int(readCsv_class.readCsv()[i][0]),
                  int(readCsv_class.readCsv()[i][1]),
                  int(readCsv_class.readCsv()[i][2]),
                  readCsv_class.readCsv()[i][3], '>>>>>>验证成功!')


if __name__ == '__main__':
    unittest.main()
