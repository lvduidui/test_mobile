import time

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy


class TestDW:
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "7.1.2",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            # 下次启动app时,不重置app.保留上次缓存.
            "noReset": "true",
            "dontStopAppOnreset": "true",
            "skipDeviceInitialization": "true"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize()
    def test_search(self):
        '''
        参数化搜索多个股票
        :return:
        '''
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/home_search').click()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')

