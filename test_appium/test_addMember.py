import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddMember:
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "7.1.2",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            # 下次启动app时,不重置app.保留上次缓存.
            "noReset": "true",
            "dontStopAppOnreset": "true",
            "skipDeviceInitialization": "true"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # time.sleep(3)
        # self.driver.quit()
        pass

    #添加成员
    def test_add_member(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        # 当添加成员多了之后,需要滑动查找添加成员按钮
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/cox"]').click()

        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/b4t"]').send_keys('李白')
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/b5v"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/bdz"]').click()

        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/fow"]').send_keys('18912345678')
        self.driver.find_element(MobileBy.XPATH,'//*[@text="设置部门"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="王者荣耀"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"确定")]').click()

        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/fco"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/i6k"]').click()
        time.sleep(1)
        self.driver.back()

        #获取toast来断言
        self.driver.find_element(MobileBy.XPATH,'//*[@text="王者荣耀"]').click()
        elements = self.driver.find_elements(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/icn"]/android.widget.TextView')
        elements_list = []
        for e in elements:
            elements_list.append(e.text)

        assert '李白' in elements_list





