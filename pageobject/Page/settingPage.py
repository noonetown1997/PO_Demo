from Base.Base import Base
from Page.pageElements import PageElements


class SettingPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def logout(self, tag=1):
        """
        退出
        :param tag: 1:确认退出 2:取消退出
        :return:
        """
        # 向上滑动页面
        self.scroll_screen()
        # 点击退出按钮
        self.click_element(PageElements.setting_logout_id)
        if tag == 1:
            self.click_element(PageElements.setting_logout_acc_id)
        else:
            self.click_element(PageElements.setting_logout_dis_id)

    def click_address_btn(self):
        """点击地址管理"""
        self.click_element(PageElements.setting_address_btn_id)
