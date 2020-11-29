"""
购物车页面
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


class GoodsCartPage(BasePage):
    """购物车-对象库层"""

    def __init__(self):
        super().__init__()  # 获取浏览器对象

        self.check_all = (By.CLASS_NAME, 'checkCartAll')  # 全选复选框
        self.go_pay_btn = (By.LINK_TEXT, '去结算')  # 去结算按钮

    def find_check_all(self):
        """全选复选框定位方法"""
        return self.find_element_func(self.check_all)

    def find_go_pay_btn(self):
        """去结算按钮定位方法"""
        return self.find_element_func(self.go_pay_btn)


class GoodsCartHandle(BaseHandle):
    """购物车-操作层"""

    def __init__(self):
        self.goods_cart_page = GoodsCartPage()  # 元素定位对象

    def click_check_all(self):
        """全选框点击方法"""
        check_all_element = self.goods_cart_page.find_check_all()
        # 此处需要判断元素为未选中状态, 再做选中操作
        if not check_all_element.is_selected():
            # self.click_element(self.goods_cart_page.find_check_all())
            self.click_element(check_all_element)

    def click_go_pay_btn(self):
        """去结算按钮点击方法"""
        self.click_element(self.goods_cart_page.find_go_pay_btn())


class GoodsCartProxy(object):
    """购物车-业务层"""

    def __init__(self):
        self.goods_cart_handle = GoodsCartHandle()  # 操作对象

    def go_to_order_check(self):
        """跳转订单确认页面方法"""
        self.goods_cart_handle.click_check_all()  # 点击全选
        self.goods_cart_handle.click_go_pay_btn()  # 点击结算按钮
