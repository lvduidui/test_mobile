from selenium.webdriver.common.by import By

from test_framework.basepage import BasePage
from test_framework.page.search_page import SearchPage


class MainPage(BasePage):
    def goto_search(self):
        self.find_and_click((By.ID, 'post_status'))
        self.find_and_click((By.ID, 'home_search'))
        return SearchPage(self.driver)
