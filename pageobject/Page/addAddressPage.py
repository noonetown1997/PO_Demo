from Base.Base import Base

from Page.pageElements import PageElements


class AddAddressPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def add_address(self, name=None, phone=None, area=None, detail=None, code=None, isdefault=None):
        """
        新增地址
        :param name: 收件人
        :param phone: 手机号
        :param area: 所在地区 ("省","市","区")
        :param detai: 详细地址
        :param code: 邮编
        :param isdefault: 是否默认
        :return:
        """
        # 收件人
        if name:
            self.send_element(PageElements.add_address_recv_name_id, name)
        # 手机号
        if phone:
            self.send_element(PageElements.add_address_phone_id, phone)
        # 所在地区
        if area:
            self.click_element(PageElements.add_address_select_id)
            # 选择省
            self.click_element((PageElements.add_address_select_prov_xpath[0],
                                PageElements.add_address_select_prov_xpath[1] % area[0]))
            # 选择市
            self.click_element((PageElements.add_address_select_city_xpath[0],
                                PageElements.add_address_select_city_xpath[1] % area[1]))
            # 选择区
            if area[2]:
                # 选择区
                self.click_element((PageElements.add_address_select_area_xpath[0],
                                    PageElements.add_address_select_area_xpath[1] % area[2]))
        # 详细地址
        if detail:
            self.send_element(PageElements.add_address_detail_id, detail)
        # 邮编
        if code:
            self.send_element(PageElements.add_address_post_code_id, code)
        # 是否默认
        if isdefault:
            self.click_element(PageElements.add_address_default_id)
        # 点击保存
        self.click_element(PageElements.add_address_save_btn_id)
