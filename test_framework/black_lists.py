'''
处理弹窗广告,加入黑名单
'''

# 加入黑名单
from selenium.webdriver.common.by import By


def handle_black(func):
    black_lists = [(By.ID, 'iv_close')]

    def run(*args, **kwargs):
        # self
        item = args[0]
        try:
            return func(*args, **kwargs)
        except Exception as e:
            for black in black_lists:
                eles = item.driver.find_elements(*black)
                if len(eles) > 0:
                    # 关闭弹窗
                    eles[0].click()
                    # 再次查找
                return func(*args, **kwargs)

            raise e

    return run
