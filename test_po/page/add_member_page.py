from appium.webdriver.common.mobileby import MobileBy

from test_po.page.add_member_edit_page import AddMemberEditPage
from test_po.page.basepage import BasePage


class AddMemberPage(BasePage):
    def goto_add_member_edit_page(self):
        self.find_and_click((MobileBy.XPATH, '//*[@text="手动输入添加"]'))
        return AddMemberEditPage(self.driver)

    def get_toast(self):
        ele_text = self.find_and_getText((MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))

        return ele_text
