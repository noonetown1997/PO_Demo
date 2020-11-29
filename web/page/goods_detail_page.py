"""
商品详情页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class GoodsDetailPage(BasePage):
    """商品详情-对象库层"""

    def __init__(self):
        super().__init__()  # 获取浏览器对象

        self.join_cart_btn = (By.ID, 'join_cart')  # 加入购物车按钮
        self.join_cart_result = (By.CSS_SELECTOR, '.conect-title')  # 加入购物车结果

    def find_join_cart_btn(self):
        """加入购物车按钮定位方法"""
        return self.find_element_func(self.join_cart_btn)

    def find_join_cart_result(self):
        """加入购物车结果定位方法"""
        return self.find_element_func(self.join_cart_result)


class GoodsDetailHandle(BaseHandle):
    """商品详情-操作层"""

    def __init__(self):
        self.goods_detail_page = GoodsDetailPage()  # 元素定位对象

    def click_join_cart_btn(self):
        """加入购物车按钮点击方法"""
        self.click_element(self.goods_detail_page.find_join_cart_btn())

    def get_join_cart_result(self):
        """获取加入购物结果方法"""
        # 切换 frame
        driver = DriverUtil.get_driver()  # 获取浏览器对象
        # 注意: 切换 frame 操作也可以使用定位到的 iframe 元素对象
        driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
        return self.goods_detail_page.find_join_cart_result().text


class GoodsDetailProxy(object):
    """商品详情-业务层"""

    def __init__(self):
        self.goods_detail_handle = GoodsDetailHandle()  # 操作对象

    def add_goods_to_cart(self):
        """添加商品到购物车方法"""
        self.goods_detail_handle.click_join_cart_btn()

    def get_join_result(self):
        """获取加入购物车结果方法"""
        return self.goods_detail_handle.get_join_cart_result()
