"""
程序入口-测试套件
"""
import time
import unittest
from case.test_cart import TestCart
from case.test_login import TestLogin
from case.test_order import TestOrder
from config import BASE_DIR
from utils import DriverUtil
from tools.HTMLTestRunnerCN import HTMLTestReportCN

# 初始化套件对象
suite = unittest.TestSuite()
# 调用方法组装测试用例
suite.addTest(unittest.makeSuite(TestLogin))  # 登录模块测试用例
suite.addTest(unittest.makeSuite(TestCart))  # 购物车模块测试用例
suite.addTest(unittest.makeSuite(TestOrder))  # 订单模块测试用例

# 关闭退出方法
DriverUtil.change_quit_status(False)

# 初始化套件执行对象, 调用套件执行方法
# unittest.TextTestRunner().run(suite)

# 设置报告存放位置及文件名
now_time = time.strftime('%Y%m%d-%H%M%S')
report_name = BASE_DIR + '/report/report_{}.html'.format(now_time)

# 打开报告写入文件流
with open(report_name, 'wb') as f:
    runner = HTMLTestReportCN(stream=f,
                              verbosity=2,
                              title='Web 自动化测试报告',
                              description='环境: 谷歌浏览器, Python 语言, macOS',
                              tester='QA10')
    runner.run(suite)

# 打开退出方法
DriverUtil.change_quit_status(True)

# 调用退出方法
DriverUtil.quit_driver()
