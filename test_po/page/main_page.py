from appium.webdriver.common.mobileby import MobileBy

from test_po.page.basepage import BasePage
from test_po.page.contact_page import ContactPage


class MainPage(BasePage):

    def goto_contactPage(self):
        self.find_and_click((MobileBy.XPATH, '//*[@text="通讯录"]'))

        return ContactPage(self.driver)
