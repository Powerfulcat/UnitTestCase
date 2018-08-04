# 导包
import unittest
import time

from Tools.HTMLTestReportCN import HTMLTestRunner

if __name__ == '__main__':
    # 1.组装测试用例case
    case_dir = './Case/'
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test_*.py')

    # 2.准备报告生成的路径
    report_dir = './Report/'
    # 3.获取当前时间
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    # 4.设置报告名称
    report_name = report_dir + now_time + 'Report.html'
    print(report_name)
    # 打开报告写入文件流
    with open(report_name, 'wb') as f:
        # 初始化报告生成对象
        runner = HTMLTestRunner(stream=f, verbosity=2, title='单元测试报告', description='运行环境：macOS，执行人：test04QA')
        runner.run(discover)
