'''
封装通用用例步骤
'''
from test_framework.app import App


class TestBase:

    #初始化app
    def setup(self):
        self.app = App()
