from pprint import pprint

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from test_framework.black_lists import handle_black


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, locator):
        return self.driver.find_element(*locator)

    # 找到并点击
    def find_and_click(self, locator):
        self.find(locator).click()

    # 找到并获取文本
    def find_and_getText(self, locator):
        return self.find(locator).text

    # 封装send_keys
    def send(self,locator,content):
        self.find(locator).send_keys(content)

    # 滑动找到元素并点击
    def scroll_and_click(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiScrollable(new UiSelector().'
               'scrollable(true).instance(0)).'
               'scrollIntoView(new UiSelector().'
               f'text("{text}").instance(0));')
        self.find_and_click(ele)

    # 解析yaml文件,实现关键字驱动
    def  run_keys(self,path,operation=None):
        with open(path,'r',encoding='utf-8') as f:
            data = yaml.safe_load(f)

        keys = data[operation]
        # print(keys)

        for key in keys:
            action = key['action']
            if action == 'find_and_click':
                self.find_and_click(key['locator'])
            elif action == 'send':
                self.send(key['locator'],key['content'])



if __name__ == '__main__':

    BasePage().run_keys('page/main_page.yaml','goto_market')