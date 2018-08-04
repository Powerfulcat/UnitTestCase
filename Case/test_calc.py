import unittest
# 导包calc
# from Func.calc import Calc
from Func.calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_calc_add(self):
        result = Calc().add(10, 20)
        print('add:', result)
        # 断言
        self.assertEqual(30, result)

    def test_calc_sub(self):
        result = Calc().sub(10, 5)
        print('sub:', result)
        # 断言
        self.assertEqual(5, result)


if __name__ == '__main__':
    unittest.main()

# 注意:
# 在UnitTest框架下,所有的自定义测试方法都是独立执行的,任何一个方法的成功与否都不会影响其他方法的执行
