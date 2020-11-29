"""
订单支付页面
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


class OrderPayPage(BasePage):
    """订单支付-对象库层"""

    def __init__(self):
        super().__init__()  # 获取浏览器对象

        self.after_pay = (By.CSS_SELECTOR, '[value="pay_code=cod"]')  # 货到付款
        self.confirm_pay = (By.LINK_TEXT, '确认支付方式')  # 确认支付

    def find_after_pay(self):
        """货到付款定位方法"""
        return self.find_element_func(self.after_pay)

    def find_confirm_pay(self):
        """确认支付定位方法"""
        return self.find_element_func(self.confirm_pay)


class OrderPayHandle(BaseHandle):
    """订单支付-操作层"""

    def __init__(self):
        self.order_pay_page = OrderPayPage()  # 元素定位对象

    def click_after_pay(self):
        """货到付款点击方法"""
        self.click_element(self.order_pay_page.find_after_pay())

    def click_confirm_pay(self):
        """确认支付点击方法"""
        self.click_element(self.order_pay_page.find_confirm_pay())


class OrderPayProxy(object):
    """订单支付-业务层"""

    def __init__(self):
        self.order_pay_handle = OrderPayHandle()  # 操作对象

    def order_pay(self):
        """订单支付方法"""
        self.order_pay_handle.click_after_pay()  # 选择货到付款
        self.order_pay_handle.click_confirm_pay()  # 确认支付
