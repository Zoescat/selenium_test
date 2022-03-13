from time import  sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util.util import get_code,identification_verification_code

class TestAdminLogin(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://192.168.50.5:8080/admin/login')
        self.driver.maximize_window()
        sleep(2)
        
           
    # 测试用户名为空的场景
    def test_admin_login_code_error(self):
        user='zoe'
        pwd='123456'
        # 输入错误的验证码
        captcha='asd1'
        excepted='验证码不正确，请重新输入'
        
        self.driver.find_element_by_name('user').send_keys(user)
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 输入验证码
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        
        # Python的断言
        assert alert.text==excepted
        alert.accept()
        sleep(5)
        
        
    # 测试管理员登录成功的场景
    def test_admin_login_success(self):
        user='zoe'
        pwd='xiaoweiba'
        excepted='JPress后台'
        
        # 输入用户名
        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(user)
        # 输入密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 自动识别验证码并保存
        captcha_picture=get_code(self.driver,'captcha-img')
        captcha=identification_verification_code(captcha_picture)
        print('识别的验证码是:',captcha)
        # 输入验证码
        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册
        self.driver.find_element_by_class_name('btn').click()
        # 
        WebDriverWait(self.driver,2).until(EC.title_is(excepted))   
        # Python的断言
        assert  excepted==self.driver.title
    
        
    
        