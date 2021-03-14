from appium import webdriver

# desired_caps = {}
# desired_caps['platformName']='Android'
# desired_caps['platformVersion']='7.1.2'
# desired_caps['deviceName']='127.0.0.1:62001'
# desired_caps['appPackage']='com.android.settings'
# desired_caps['appActivity']='com.android.settings.Settings'
# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

# windows获取apppackage和appactivity, adb logcat|findstr -i displayed
desired_caps = {
    "platformName": "android",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    # 下次启动app时,不重置app.保留上次缓存.
    "noReset": True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
el2 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("腾讯")
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.LinearLayout")
el4.click()
