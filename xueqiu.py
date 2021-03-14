from appium import webdriver

desired_caps = {
    "platformName": "android",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    # 下次启动app时,不重置app.保留上次缓存.
    "noReset": "true",
    "dontStopAppOnreset": "true",
    "skipDeviceInitialization": "true"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("腾讯")
driver.back()
driver.back()
