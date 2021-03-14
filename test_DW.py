import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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
        time.sleep(2)
        self.driver.quit()


    # def test_search(self):
    #     print('获取阿里巴巴股价,并判断股价>200')
    #     self.driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
    #     self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
    #     self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
    #     current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
    #     assert current_price > 200

    # def test_attr(self):
    #     #获取属性值
    #     ele = self.driver.find_element_by_id('com.xueqiu.android:id/home_search')
    #     print(ele.text)
    #     print(ele.location)
    #     print(ele.size)
    #     if ele.is_enabled():
    #         ele.click()
    #     self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
    #     ele2 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
    #     ele2_display = ele2.get_attribute('displayed')
    #     if ele2_display == 'true':
    #         print('搜索成功')
    #     else:
    #         print('搜索失败')

    # def test_touchaction(self):
    #     # 滑动
    #     time.sleep(10)
    #     action = TouchAction(self.driver)
    #     widow_rect = self.driver.get_window_rect()
    #     width = widow_rect['width']
    #     height = widow_rect['height']
    #     x1 = int(width/2)
    #     y_start = int(height*4/5)
    #     y_end = int(height*1/5)
    #     action.press(x=x1,y=y_start).wait(2000).move_to(x=x1,y=y_end).release().perform()

    # def test_myinfo(self):
        '''
        登录
        :return:
        '''
        # 父节点,兄弟节点,.childSelector .fromParent
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('18952072925')
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('1qaz@WSX')
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        #
        # assert self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/my_home_page")').text == '我的主页'

    def test_scroll_findElement(self):
        # 滚动查找元素
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).'
                                                        'instance(0)).scrollIntoView(new UiSelector().text("杭州王大磊").instance(0));')
        time.sleep(2)


if __name__ == '__main__':
    pytest.main(['-sv', 'test_DW.py'])
