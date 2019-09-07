from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time, allure, os


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元祖 (By.ID, 属性值) (By.XPATH, 属性值) (By.CLASS_NAME, 属性值)
        :param timeout: 搜索超时时间
        :param poll_frequency: 搜索间隔
        :return: 返回元素定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: 元祖 (By.ID, 属性值) (By.XPATH, 属性值) (By.CLASS_NAME, 属性值)
        :param timeout: 搜索超时时间
        :param poll_frequency: 搜索间隔
        :return: 返回元素定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        """
        点击元素
        :param loc: 元祖 (By.ID, 属性值) (By.XPATH, 属性值) (By.CLASS_NAME, 属性值)
        :return:
        """
        self.get_element(loc).click()

    def send_element(self, loc, text):
        """
        输入文本内容
        :param loc: 元祖 (By.ID, 属性值) (By.XPATH, 属性值) (By.CLASS_NAME, 属性值)
        :param text: 需要输入的内容
        :return:
        """
        # 定位
        input_text = self.get_element(loc)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)

    def scroll_screen(self, tag=1):
        """
        滑动操作
        :param tag: 1:向上 2:向下 3:向左 4:向右
        :return:
        """
        # 取分辨率
        screen = self.driver.get_window_size()
        # 取宽
        width = screen.get("width")
        # 取高
        height = screen.get("height")
        # 防止页面未跳转 直接滑动
        time.sleep(2)
        # 根据宽高百分比滑动
        if tag == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, duration=2000)
        if tag == 2:
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, duration=2000)
        if tag == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, duration=2000)
        if tag == 4:
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, duration=2000)

    def get_toast(self, message):
        """
        获取toast提示消息
        :param message: 拼接xpath使用文本
        :return: toast全部内容
        """
        # 获取toast消息
        mess_xpath = "//*[contains(@text,'%s')]" % message
        return self.get_element((By.XPATH, mess_xpath), timeout=3, poll_frequency=0.3).text

    def get_screenshot(self, name="截图"):
        """截图"""
        # 截图名字
        png_name = "./image" + os.sep + "%d.png" % int(time.time())
        self.driver.get_screenshot_as_file(png_name)
        # 添加图片
        with open(png_name, "rb") as f:

            allure.attach(name, f.read(), allure.attach_type.PNG)
