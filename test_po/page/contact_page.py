from appium.webdriver.common.mobileby import MobileBy

from test_po.page.add_member_page import AddMemberPage
from test_po.page.basepage import BasePage


class ContactPage(BasePage):

    def goto_add_member_page(self):
        # self.find_and_click((MobileBy.XPATH, '//*[@text="添加成员"]'))
        self.scroll_and_click("添加成员")

        return AddMemberPage(self.driver)
