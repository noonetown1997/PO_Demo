from Base.Base import Base
from Page.pageElements import PageElements


class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, user, passwd):
        """
        登录操作
        :param user: 账户
        :param passwd: 密码
        :return:
        """
        # 输入账号
        self.send_element(PageElements.login_user_id, user)
        # 输入密码
        self.send_element(PageElements.login_passwd_id, passwd)
        # 点击登录
        self.click_element(PageElements.login_btn_id)

    def if_login_btn(self):
        """
        判断登录按钮是否存在
        :return: 存在返回True 不存在返回False
        """
        try:
            # 定位登录按钮
            self.get_element(PageElements.login_btn_id)
            return True
        except:
            return False

    def close_login_page(self):
        """关闭登录页面"""
        self.click_element(PageElements.login_close_btn)
