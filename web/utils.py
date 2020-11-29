"""
公共方法类
"""
from time import sleep
from selenium import webdriver


def switch_to_new_window():
    """切换新窗口方法"""
    driver = DriverUtil.get_driver()
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])


def get_text_element(text):
    """定位特定文本元素的方法"""
    xpath = '//*[contains(text(),"{}")]'.format(text)
    try:
        element = DriverUtil.get_driver().find_element_by_xpath(xpath)
        return element
    except Exception as e:
        return False


class DriverUtil(object):
    """浏览器工具类"""
    _driver = None

    _auto_quit = True

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.get('http://127.0.0.1')
            cls._driver.maximize_window()  # 窗口最大化
            cls._driver.implicitly_wait(10)  # 隐式等待
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        if cls._driver and cls._auto_quit:
            cls._driver.quit()
            cls._driver = None

    @classmethod
    def change_quit_status(cls, auto):
        """修改退出方法状态方法"""
        cls._auto_quit = auto


if __name__ == '__main__':
    DriverUtil.get_driver()
    sleep(3)
    DriverUtil.quit_driver()
