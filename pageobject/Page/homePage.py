from Base.Base import Base
from Page.pageElements import PageElements


class HomePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)


    def click_my_btn(self):
        """点击首页 我按钮"""
        self.click_element(PageElements.home_my_btn_id)
