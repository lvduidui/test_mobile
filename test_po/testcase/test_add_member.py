import os

import pytest

from test_po.Utils.get_data import get_datas
from test_po.page.app import App

data_path = os.path.dirname(os.path.dirname(__file__)) + '/data/data.yaml'


# print(data_path)


class TestAddMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phonenum", get_datas(data_path))
    def test_add_member(self, name, gender, phonenum):
        toast_text = self.main.goto_contactPage().goto_add_member_page().goto_add_member_edit_page() \
            .edit_name(name).select_gender(gender). \
            edit_phoneNum(phonenum).click_save_button().get_toast()

        assert toast_text == '添加成功'
