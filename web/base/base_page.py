"""
page 文件的基类
"""
from utils import DriverUtil


class BasePage(object):
    """对象库层-基类"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def find_element_func(self, location):
        """
        元素定位方法
        :param location: 元素属性
        :return: 元素对象
        """
        # return self.driver.find_element(location[0], location[1])
        # 利用拆包(解包)完成参数的数据的获取
        return self.driver.find_element(*location)


class BaseHandle(object):
    """操作层-基类"""

    @staticmethod
    def input_text(element, text):
        """输入内容方法"""
        element.clear()
        element.send_keys(text)

    @staticmethod
    def click_element(element):
        """元素点击方法"""
        element.click()
