import unittest
from Func.triangle import Triangle
from ReadData.read_txt import ReadTxt

triangle_class = Triangle()
readTxt_class = ReadTxt()


class TestTriangleTxt(unittest.TestCase):
    def test_triangleTxt(self):
        # 遍历
        for i in range(len(readTxt_class.readTxt())):
            result = triangle_class.func_triangle(int(readTxt_class.readTxt()[i][0]),
                                                  int(readTxt_class.readTxt()[i][1]),
                                                  int(readTxt_class.readTxt()[i][2]))
            # 设置断言
            self.assertEqual(result, readTxt_class.readTxt()[i][3])

            # 打印
            print(result)
            print(int(readTxt_class.readTxt()[i][0]),
                  int(readTxt_class.readTxt()[i][1]),
                  int(readTxt_class.readTxt()[i][2]),
                  readTxt_class.readTxt()[i][3])


if __name__ == '__main__':
    unittest.main()
