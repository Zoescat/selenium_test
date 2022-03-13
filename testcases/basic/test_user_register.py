from time import  sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util.util import get_code,identification_verification_code,gen_random_str



class TestUserRegister(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://192.168.50.5:8080/user/register')
        self.driver.maximize_window()
        sleep(2)
        
        
    
    # 测试验证码错误的场景
    def test_register_code_error(self):
        username='test001'
        email='test001@qq.com'
        pwd='123456'
        confirmPwd='123456'
        captcha='666'
        excepted='验证码不正确'
        
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('email').send_keys(email)
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        
        # Python的断言
        assert alert.text==excepted
        alert.accept()
        sleep(5)
        
        
    # 测试注册成功的场景
    def test_register_success(self):
        username=gen_random_str()
        email=username+'@qq.com'
        pwd='123456'
        confirmPwd='123456'
        excepted='注册成功，点击确定进行登录'
        
        # 输入用户名
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)
        # 输入邮箱
        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(email)
        # 输入密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        # 自动识别验证码并保存
        captcha_picture=get_code(self.driver,'captcha-img')
        captcha=identification_verification_code(captcha_picture)
        print('识别的验证码是：',captcha)
        # 输入验证码
        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册
        self.driver.find_element_by_class_name('btn').click()
        # 等待alert的出现 
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
            
        # Python的断言
        assert alert.text==excepted
        alert.accept()
        sleep(5)
    
        