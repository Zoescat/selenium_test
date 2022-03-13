import allure
import pytest

@pytest.fixture(scope='session')
def login():
    print('用例先登录')
    

@allure.step('步骤1:点xxx')
def step_1():
    print('第一步。。。')
    

@allure.step('步骤2:点xxx')
def step_2():
    print('第二步。。。')
    
    
@allure.feature('编辑页面')
class TestEditPage():
    '''编辑页面'''
    @allure.story('这是一个xxx的用例')
    def test_1(self,login):
        '''用例描述:先登录,再去执行xxx'''
        step_1()
        step_2()
        print('编辑页面...')
        
    @allure.story('打开xxx页面')
    def test_2(self,login):
        '''用例描述:先登录,再去执行yyy'''
        print('打开xxx页面中。。。')
        
        
if __name__ == '__main__':
    # 注意生成测试报告，必须在命令执行行执行
    # 1. pytest --alluredir ./reports/
    # 2. allure serve ./reports 启动allure 查看报告
    pytest.main(['--alluredir','./reports','allure_demo1.py'])

    
