import sys, os, pytest, time

sys.path.append(os.getcwd())

from Base.Page import Page
from Base.getDriver import get_android_driver
from Base.getFile import GetFile
from selenium.common.exceptions import TimeoutException


def data():
    # 成功数据列表
    suc_list = []
    # 失败数据列表
    fail_list = []
    # 实例化读文件数据
    value = GetFile().get_yml_data("login_data.yml")
    for i in value.keys():
        if value.get(i).get("toast"):
            """失败数据"""
            fail_list.append((i, value.get(i).get("user"), value.get(i).get("passwd"),
                              value.get(i).get("toast"), value.get(i).get("exp_data")))
        else:
            """成功数据"""
            suc_list.append((i, value.get(i).get("user"), value.get(i).get("passwd"),
                             value.get(i).get("exp_data")))

    return {"suc": suc_list, "fail": fail_list}


class TestLogin:

    def setup_class(self):
        # 实例化统一入口类
        self.page_obj = Page(get_android_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

    def teardown_class(self):
        time.sleep(3)
        # 退出driver
        self.page_obj.driver.quit()

    def logout(self):
        # 个人中心点击设置
        self.page_obj.get_person_page().click_setting_btn()
        # 设置页面点击退出
        self.page_obj.get_setting_page().logout()

    @pytest.fixture(autouse=True)
    def goto_login_page(self):
        """进入登录页面"""
        # 点击我
        self.page_obj.get_home_page().click_my_btn()
        # 点击已有账号去登录
        self.page_obj.get_choice_login_page().click_exits_account()

    @pytest.mark.parametrize("case_num, user, passwd, exp_data", data().get("suc"))
    def test_login_suc(self, case_num, user, passwd, exp_data):
        """
        预期成功测试用例
        :param case_num: 用例编号
        :param user: 账号
        :param passwd: 密码
        :param exp_data: 预期结果
        :return:
        """
        # 登录
        self.page_obj.get_login_page().login(user, passwd)
        try:
            # 我的优惠券-查找
            shop_cart = self.page_obj.get_person_page().get_shop_cart()
            try:
                # 断言
                assert shop_cart == exp_data
            except AssertionError:
                # 截图 TODO
                self.page_obj.get_person_page().get_screenshot()
                assert False
            finally:
                # 退出操作
                self.logout()
        except TimeoutException:
            # 截图 TODO
            self.page_obj.get_setting_page().get_screenshot()
            if self.page_obj.get_login_page().if_login_btn():
                # 关闭登录页面
                self.page_obj.get_login_page().close_login_page()
            else:
                # 退出操作
                self.logout()
            assert False

    @pytest.mark.parametrize("case_num, user, passwd, toast, exp_data", data().get("fail"))
    def test_login_fail(self, case_num, user, passwd, toast, exp_data):
        """
        预期失败测试用例
        :param case_num: 用例编号
        :param user: 账号
        :param passwd: 密码
        :param toast: 获取toast消息拼接xpath
        :param exp_data: 预期结果
        :return:
        """
        # 登录
        self.page_obj.get_login_page().login(user, passwd)
        try:
            # 获取toast
            message = self.page_obj.get_login_page().get_toast(toast)
            try:
                # 断言toast
                assert message == exp_data
            except AssertionError:
                # 断言失败
                # 截图
                self.page_obj.get_login_page().get_screenshot()
                assert False
        except TimeoutException:
            # 找不到toast消息
            # 截图
            self.page_obj.get_login_page().get_screenshot()
            assert False
        finally:
            try:
                # 断言登录
                assert self.page_obj.get_login_page().if_login_btn()
                # 关闭登录页面
                self.page_obj.get_login_page().close_login_page()
            except AssertionError:
                # 不再登录页面
                # 退出操作
                self.logout()
                assert False
