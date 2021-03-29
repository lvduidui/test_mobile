from selenium.webdriver.common.by import By

from test_framework.basepage import BasePage
from test_framework.page.market_page import MarketPage
from test_framework.page.search_page import SearchPage


class MainPage(BasePage):
    def goto_search(self):
        self.find_and_click((By.ID, 'post_status'))
        self.find_and_click((By.ID, 'home_search'))
        return SearchPage(self.driver)

    def goto_market(self):
        self.run_keys('../page/main_page.yaml','goto_market')
        return MarketPage(self.driver)


