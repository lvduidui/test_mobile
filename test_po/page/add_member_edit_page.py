from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.page.basepage import BasePage


class AddMemberEditPage(BasePage):
    def edit_name(self,name):
        self.find((MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/b4t"]')).send_keys(name)
        return self

    def select_gender(self,gender):
        locator = (MobileBy.XPATH, "//*[@text='男']")
        # 添加显示等待,等待选择性别出现
        ele = WebDriverWait(self.driver, 10).\
            until(expected_conditions.element_to_be_clickable(locator))
        ele.click()
        if gender == '女':
            self.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
        else:
            self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))

        return self

    def edit_phoneNum(self,phoneNum):
        self.find((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/fow"]')).send_keys(phoneNum)
        return self

    def select_department(self):
        pass

    def click_save_button(self):
        from test_po.page.add_member_page import AddMemberPage

        self.find_and_click((MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/i6k"]'))
        return AddMemberPage(self.driver)

