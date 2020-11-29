"""
登录模块-测试用例
"""
import json
import time
import unittest
import logging

from base import *
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil
from parameterized import parameterized


def build_login_data():
    """登录数据构造方法"""
    with open(BASE_DIR + '/data/login_data.json', encoding='utf-8') as f:
        data = json.load(f)
        # 声明空列表
        data_list = list()
        for i in data.values():
            data_list.append((i.get('username'),
                              i.get('password'),
                              i.get('code'),
                              i.get('expect')))
        print(data_list)
        logging.info(data_list)
        return data_list


class TestLogin(unittest.TestCase):
    """登录测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 首页业务执行对象
        cls.login_proxy = LoginProxy()  # 登录页业务执行对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1')  # 打开首页
        self.index_proxy.go_to_login_page()  # 点击登录方法

    @parameterized.expand(build_login_data())
    def test_login(self, username, pwd, code, expect):
        """登录测试方法"""
        self.login_proxy.login(username, pwd, code)  # 执行登录
        time.sleep(3)
        # 断言判定结果
        # 获取页面标题
        title = self.driver.title
        print('title=', title)
        logging.info('title=', title)
        try:
            self.assertIn(expect, title)
        except AssertionError as e:
            # 截图
            now_time = time.strftime('%Y-%m-%d %H_%M_%S')
            self.driver.get_screenshot_as_file(BASE_DIR + '/screenshot/bug_{}.png'.format(now_time))
            raise e

    # def test_login(self):
    #     """登录测试方法"""
    #     self.login_proxy.login('13800001111', '123456', '8888')  # 执行登录
    #     time.sleep(3)
    #     # 断言判定结果
    #     # 获取页面标题
    #     title = self.driver.title
    #     print('title=', title)
    #     self.assertIn('我的账户', title)


if __name__ == '__main__':
    unittest.main()
