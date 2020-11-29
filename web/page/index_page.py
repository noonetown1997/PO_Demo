"""
首页页面
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


class IndexPage(BasePage):
    """首页-对象库层"""

    def __init__(self):
        super().__init__()  # 获取浏览器对象

        self.login_link = (By.LINK_TEXT, '登录')  # 登录链接
        self.search_bar = (By.ID, 'q')  # 搜索框
        self.search_btn = (By.CLASS_NAME, 'ecsc-search-button')  # 搜索按钮
        self.my_cart_btn = (By.CLASS_NAME, 'share-shopcar-index')  # 购物车按钮
        self.my_order_link = (By.LINK_TEXT, '我的订单')  # 我的订单链接

    def find_login_link(self):
        """登录链接定位方法"""
        return self.find_element_func(self.login_link)

    def find_search_bar(self):
        """搜索框定位方法"""
        return self.find_element_func(self.search_bar)

    def find_search_btn(self):
        """搜索按钮定位方法"""
        return self.find_element_func(self.search_btn)

    def find_my_cart_btn(self):
        """我的购物车按钮定位方法"""
        return self.find_element_func(self.my_cart_btn)

    def find_my_order_link(self):
        """我的订单链接定位方法"""
        return self.find_element_func(self.my_order_link)


class IndexHandle(BaseHandle):
    """首页-操作层"""

    def __init__(self):
        self.index_page = IndexPage()  # 元素定位对象

    def click_login_link(self):
        """登录链接点击方法"""
        self.click_element(self.index_page.find_login_link())

    def input_search_bar(self, kw):
        """搜索框输入方法"""
        self.input_text(self.index_page.find_search_bar(), kw)

    def click_search_btn(self):
        """搜索按钮点击方法"""
        self.click_element(self.index_page.find_search_btn())

    def click_my_cart_btn(self):
        """我的购物车点击方法"""
        self.click_element(self.index_page.find_my_cart_btn())

    def click_my_order_link(self):
        """我的订单链接点击方法"""
        self.click_element(self.index_page.find_my_order_link())


class IndexProxy(object):
    """首页-业务层"""

    def __init__(self):
        self.index_handle = IndexHandle()  # 操作对象

    def go_to_login_page(self):
        """跳转登录页面的方法"""
        self.index_handle.click_login_link()

    def go_to_search_list(self, kw):
        """跳转搜索列表页面方法"""
        self.index_handle.input_search_bar(kw)  # 输入商品名称
        self.index_handle.click_search_btn()  # 点击搜索按钮

    def go_to_goods_cart(self):
        """跳转购物车页面方法"""
        self.index_handle.click_my_cart_btn()

    def go_to_my_order(self):
        """跳转我的订单页面方法"""
        self.index_handle.click_my_order_link()
