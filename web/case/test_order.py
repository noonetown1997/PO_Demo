"""
订单模块-测试用例
(此用例无法独立执行, 需要依赖登录和购物车测试用例执行)
"""
import unittest

from page.goods_cart_page import GoodsCartProxy
from page.index_page import IndexProxy
from page.my_order_page import MyOrderProxy
from page.order_check_page import OrderCheckProxy
from page.order_pay_page import OrderPayProxy
from utils import DriverUtil, get_text_element, switch_to_new_window


class TestOrder(unittest.TestCase):
    """订单测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 首页业务执行对象
        cls.goods_cart_proxy = GoodsCartProxy()  # 购物车业务执行对象
        cls.order_check_proxy = OrderCheckProxy()  # 订单确认业务执行对象
        cls.my_order_proxy = MyOrderProxy()  # 我的订单业务执行对象
        cls.order_pay_proxy = OrderPayProxy()  # 订单支付业务执行对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1')  # 打开首页

    def test_order(self):
        """提交订单测试方法"""
        self.index_proxy.go_to_goods_cart()  # 跳转我的购物车
        self.goods_cart_proxy.go_to_order_check()  # 点击去结算
        self.order_check_proxy.go_to_order_pay()  # 提交订单
        # 断言判定结果
        result = get_text_element('订单提交成功')
        self.assertTrue(result)

    def test_pay(self):
        """订单支付测试方法"""
        self.index_proxy.go_to_my_order()  # 点击我的订单

        # 切换窗口
        # handles = self.driver.window_handles
        # self.driver.switch_to.window(handles[-1])
        switch_to_new_window()

        self.my_order_proxy.go_to_order_pay()  # 点击立即支付

        # 切换窗口
        # handles = self.driver.window_handles
        # self.driver.switch_to.window(handles[-1])
        switch_to_new_window()

        self.order_pay_proxy.order_pay()  # 确认支付
        # 断言判断结果
        result = get_text_element('订单提交成功')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
