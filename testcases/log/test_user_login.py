import pytest 
from time import  sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util.util import get_code,identification_verification_code,get_logger


class TestUserLogin(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://192.168.50.5:8080/user/login')
        self.driver.maximize_window()
        self.logger=get_logger()
        self.logger.info('用户登录测试')
        
        
           
    # 测试用户名为空的场景
    def test_user_login_code_error(self):
        user='test001'
        pwd='12356'
        excepted='用户名或密码不正确'
        
        self.driver.find_element_by_name('user').send_keys(user)
        self.logger.debug('输入用户名称: %s',user)
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.logger.debug('输入密码: %s',pwd)
        # 自动识别验证码并保存
        captcha_picture=get_code(self.driver,'captcha-img')
        captcha=identification_verification_code(captcha_picture)
        print('识别的验证码是:',captcha)
        # 输入验证码
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册
        self.driver.find_element_by_class_name('btn').click()
        self.logger.debug('点击登录')

        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        try:
            assert alert.text==excepted
        except AssertionError as ae:
            self.logger.error('报错了,报错了: %s','报错了',exc_info=1)
       
        
        
    # 测试登录成功的场景
    def test_user_login_success(self):
        user='test001'
        pwd='123456'
        excepted='用户中心'
        
        # 输入用户名
        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(user)
        self.logger.debug('输入用户名称: %s',user)
        # 输入密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.logger.debug('输入密码: %s',pwd)
        # 自动识别验证码并保存
        captcha_picture=get_code(self.driver,'captcha-img')
        captcha=identification_verification_code(captcha_picture)
        print('识别的验证码是:',captcha)
        # 输入验证码
        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册
        self.driver.find_element_by_class_name('btn').click()
        self.logger.debug('点击登录')
        # 等待alert的出现 
        WebDriverWait(self.driver,5).until(EC.title_is_present())
        title=self.driver.title 
            
        # Python的断言
        try:
            assert title.text==excepted
        except AssertionError as ae:
            self.logger.error('报错了,报错了: %s','报错了',exc_info=1)
        sleep(5)
        

    
