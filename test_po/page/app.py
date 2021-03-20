'''
封装app常用的步骤,启动app,关闭app,重启app,进入首页
'''
import time

from appium import webdriver

from test_po.page.basepage import BasePage
from test_po.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            desired_caps = {
                "platformName": "android",
                "platformVersion": "7.1.2",
                "deviceName": "127.0.0.1:62001",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                # 下次启动app时,不重置app.保留上次缓存.
                "noReset": "true",
                "dontStopAppOnreset": "true",
                "skipDeviceInitialization": "true",
                # 设置页面等待空闲状态的时间为1秒
                "settings[waitForIdleTimeout]" : 1
            }
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()

        return self


    def stop(self):
        time.sleep(3)
        self.driver.quit()
        return self

    def restart(self):
        self.stop()
        self.start()


    # 首页
    def goto_main(self)->MainPage:
        return MainPage(self.driver)

