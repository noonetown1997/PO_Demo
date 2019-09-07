

from Base.Page import Page
from Base.getDriver import get_android_driver

# 声明driver
driver = get_android_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
# 实例化统一入口类
page_obj = Page(driver)
# 点击我
page_obj.get_home_page().click_my_btn()
# 点击已有账号取登录
page_obj.get_choice_login_page().click_exits_account()
# 登录操作
page_obj.get_login_page().login("13205698627", "wyz19970912")

# 个人中心 设置
page_obj.get_person_page().click_setting_btn()
# 设置页面点击地址
page_obj.get_setting_page().click_address_btn()
# 地址页面 点击新增地址
page_obj.get_address_manage_page().click_add_address()
# 新增地址页面添加一条非默认地址
page_obj.get_add_address_page().add_address(
    "hello",
    "13322221111",
    ("浙江省", "杭州市", "上城区"),
    "xi hu da dao", "666666")
# 获取当前所有用户和手机号信息
print("添加第一条地址打印当前地址列表:", page_obj.get_address_manage_page().get_name_phone())
# 获取默认对应的用户名
print("添加第一条地址打印默认地址:", page_obj.get_address_manage_page().get_default_name())

# 地址页面 点击新增地址
page_obj.get_address_manage_page().click_add_address()
# 新增地址页面添加一条非默认地址
page_obj.get_add_address_page().add_address(
    "world",
    "13888889999",
    ("广东省", "东莞", ""),
    "dong fang ming zhu", "888888")
# 获取当前所有用户和手机号信息
print("添加第二条地址打印当前地址列表:", page_obj.get_address_manage_page().get_name_phone())
# 获取默认对应的用户名
print("添加第二条地址打印默认地址:", page_obj.get_address_manage_page().get_default_name())

# 修改非默认地址为默认地址
# 点击编辑按钮
page_obj.get_address_manage_page().click_edit_btn()
# 点击第二次添加的地址修改按钮
page_obj.get_address_manage_page().click_update_btn("world")
# 选择设为默认
page_obj.get_add_address_page().add_address(isdefault=1)
# 获取默认对应的用户名
print("修改第二条地址打印默认地址:", page_obj.get_address_manage_page().get_default_name())

# 点击编辑按钮
page_obj.get_address_manage_page().click_edit_btn()
# 删除默认地址
page_obj.get_address_manage_page().click_delete_btn("world")
# 获取默认对应的用户名
print("删除默认地址后 打印新的默认地址:", page_obj.get_address_manage_page().get_default_name())
