from test_framework.basepage import BasePage


class MarketPage(BasePage):

    def goto_shares_search(self):
        self.run_keys('../page/main_page.yaml', 'goto_shares_search')

