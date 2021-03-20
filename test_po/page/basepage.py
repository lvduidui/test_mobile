from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    # 找到并点击
    def find_and_click(self, locator):
        self.find(locator).click()

    # 找到并获取文本
    def find_and_getText(self, locator):
        return self.find(locator).text

    # 滑动找到元素并点击
    def scroll_and_click(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiScrollable(new UiSelector().'
               'scrollable(true).instance(0)).'
               'scrollIntoView(new UiSelector().'
               f'text("{text}").instance(0));')
        self.find_and_click(ele)
