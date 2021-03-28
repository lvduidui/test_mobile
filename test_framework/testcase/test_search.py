from test_framework.testcase.test_base import TestBase


class TestSearch(TestBase):
    def test_search(self):
        result = self.app.start().goto_main().goto_search().search()

        assert result == True
