import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver):
        self._driver = driver


    def find(self,by,locator=None):
        # 三元表达式,如果传的是元组则拆包,否则直接位置参数一一对应
        return self._driver.find_element(*by) if isinstance(by,tuple) else self._driver.find_element(by,locator)

    def steps(self,path):
        with open(path,encoding='utf-8') as f:
            # steps列表嵌套字典
            steps:list[dict]= yaml.safe_load(f)
            for step in steps:
                if 'by' in step.keys():
                    pass
