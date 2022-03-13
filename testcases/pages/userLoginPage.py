
import imp
from time import sleep
from selenium.webdriver.common.by import By
from testcases.pom.basePage import BasePage

class UserLoginPage(BasePage):
    username_input=(By.NAME,'username')
    email_input=(By.NAME,'email')
    pwd_input=(By.NAME,'pwd')
    confirmPwd_input=(By.NAME,'confirmPwd')
    captcha_input=(By.NAME,'captcha')
    regieter_btn=(By.NAME,'btn')
    
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        
    def goto_register_page(self):
        self.driver.get('htp://192.168.50.5:8080/user/login')
        
    def input_username(self,username):
        self.clear(*self.username_input)
        self.type_text(username,*self.username_input)
        
    def input_email(self,email):
        self.clear(*self.email_input)
        self.type_text(email,*self.email_input)
        
    def input_pwd(self,pwd):
        self.clear(*self.pwd_input)
        self.type_text(pwd,*self.pwd_input)
        
    def input_confirmPwd(self,confirmPwd):
        self.clear(*self.confirmPwd_input)
        self.type_text(confirmPwd,*self.confirmPwd_input)
        
    def input_captcha(self,captcha):
        self.clear (*self.captcha_input)
        self.type_text(captcha,*self.captcha_input)
    
    def click_login_btn(self):
        self.clear(*self.click_login_btn)
        sleep(3)
        
        
        