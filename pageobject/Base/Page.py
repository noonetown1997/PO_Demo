from Page.homePage import HomePage
from Page.choiceLoginPage import ChoiceLoginPage
from Page.loginPage import LoginPage
from Page.personPage import PersonPage
from Page.settingPage import SettingPage
from Page.addressManagePage import AddressManagePage
from Page.addAddressPage import AddAddressPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        """返回首页对象"""
        return HomePage(self.driver)

    def get_choice_login_page(self):
        """返回选择登录页对象"""
        return ChoiceLoginPage(self.driver)

    def get_login_page(self):
        """返回登录页面对象"""
        return LoginPage(self.driver)

    def get_person_page(self):
        """返回个人中心页面对象"""
        return PersonPage(self.driver)

    def get_setting_page(self):
        """返回设置页面对象"""
        return SettingPage(self.driver)

    def get_address_manage_page(self):
        """返回地址管理页面"""
        return AddressManagePage(self.driver)

    def get_add_address_page(self):
        """返回新增地址页面"""
        return AddAddressPage(self.driver)
