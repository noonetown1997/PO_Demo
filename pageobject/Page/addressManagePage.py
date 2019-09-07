from Base.Base import Base

from Page.pageElements import PageElements


class AddressManagePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_name_phone(self):
        """返回所有地址的用户名和手机号"""
        name_phone = self.get_elements(PageElements.address_manage_name_phone_ids)

        return [i.text for i in name_phone]

    def get_default_name(self):
        """返回默认对应用户名和手机号"""
        return self.get_element(PageElements.address_manage_default_get_name_xpath).text

    def click_edit_btn(self):
        """点击编辑按钮"""
        self.click_element(PageElements.address_manage_edit_btn_id)

    def get_area(self):
        """返回所有地址所在地区"""
        return self.get_elements(PageElements.address_manage_area_ids)

    def click_update_btn(self, name):
        """点击修改按钮"""
        self.click_element((PageElements.address_manage_update_btn_xpath[0],
                            PageElements.address_manage_update_btn_xpath[1] % name))

    def click_delete_btn(self, name):
        """点击删除按钮"""
        self.click_element((PageElements.address_manage_delete_btn_xpath[0],
                            PageElements.address_manage_delete_btn_xpath[1] % name))
        # 确认删除
        self.click_element(PageElements.address_manage_delete_acc_btn_id)

    def click_add_address(self):
        """点击新增地址按钮"""
        self.click_element(PageElements.address_manage_add_btn_id)
