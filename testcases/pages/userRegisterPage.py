
from time import sleep
from selenium.webdriver.common.by import By
from testcases.pages.basePage import BasePage


class UserRegisterPage(BasePage):
    username_input=(By.NAME,'username')
    email_input=(By.NAME,'email')
    pwd_input=(By.NAME,'pwd')
    confirmPwd_input=(By.NAME,'confirmPwd')
    captcha_input=(By.NAME,'captcha')
    register_btn=(By.NAME,'btn')
    
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        
    def goto_register_page(self):
        self.driver.get('http://192.168.50.5:8080/user/register')
        
    def input_username(self,username):
        self.clear(self.username_input)
        self.type.text(username,*self.username_input)
        
    def input_email(self,email):
        self.clear(*self.pwd_input)
        self.type_text(email,*self.email_input)
        
    def input_pwd(self,pwd):
        self.clear(*self.pwd_input)
        self.type_text(pwd,*self.pwd_input)
        
    def input_confirmPwd(self,confirmPwd):
        self.clear(*self.input_confirmPwd)
        self.type_text(confirmPwd,*self.confirmPwd_input)
        
    def input_captcha(self,captcha):
        self.clear(*self.captcha_input)
        self.type_text(captcha,*self.captcha_input)
        
    def click_register_btn(self):
        self.clear(*self.register_btn)
        sleep(2)