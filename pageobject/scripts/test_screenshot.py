import sys, os

sys.path.append(os.getcwd())

from Base.getDriver import get_android_driver
import allure


class Test_001:

    def test_001(self):
        # 截图
        driver = get_android_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        driver.get_screenshot_as_file("./image/截图.png")

        # 添加图片
        with open("./image/截图.png", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)

        assert True
