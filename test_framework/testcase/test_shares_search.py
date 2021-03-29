from test_framework.testcase.test_base import TestBase


class TestSharesSearch(TestBase):


    def test_shares_search(self):
        self.app.goto_main().goto_market().goto_shares_search()