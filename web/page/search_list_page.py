"""
搜索列表页面
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


class SearchListPage(BasePage):
    """搜索列表-对象库层"""

    def __init__(self):
        super().__init__()  # 获取浏览器对象

        # 注意: XPath语法需要验证确认可用后, 再放入代码中
        # self.goods = (By.XPATH, '//*[@class="shop_name2"]/*[contains(text(),"小米手机5")]')  # 搜索的商品
        self.goods = (By.XPATH, '//*[@class="shop_name2"]/*[contains(text(),"{}")]')  # 搜索的商品

    def find_goods(self, kw):
        """搜索到的商品定位方法"""
        location = (self.goods[0], self.goods[1].format(kw))
        return self.find_element_func(location)


class SearchListHandle(BaseHandle):
    """搜索列表-操作层"""

    def __init__(self):
        self.search_list_page = SearchListPage()  # 元素定位对象

    def click_goods(self, kw):
        """点击搜索到的商品方法"""
        self.click_element(self.search_list_page.find_goods(kw))


class SearchListProxy(object):
    """搜索列表-业务层"""

    def __init__(self):
        self.search_list_handle = SearchListHandle()  # 操作对象

    def go_to_goods_detail(self, kw):
        """跳转商品详情页面方法"""
        self.search_list_handle.click_goods(kw)
