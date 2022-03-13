import pytest
from selenium import webdriver
from testcases import testcase1,testcase02
from util.util import identification_verification_code,get_code
from testcases.basic.test_user_register import TestUserRegister
from testcases.basic.test_user_login import TestUserLogin
from testcases.basic.test_admin_login import TestAdminLogin
from testcases.basic.test_category import TestCategory
from testcases.basic.test_article import TestArticle


if __name__ == '__main__':
    # testcase02.test1()
    # testcase02.test2()captcha
    # driver=webdriver.Chrome()  
    # driver.get('http://192.168.50.5:8080/user/register')
    # driver.maximize_window()
    # captcha_picture=get_code(driver,'captcha-img')
    # captcha=identification_verification_code(captcha_picture)
    # print(captcha)
    
    # # 用户注册
    # case001=TestUserRegister()
    # # case001.test_register_code_error()
    # case001.test_register_success()
    
    # 用户登录
    # case02=TestUserLogin()
    # # case02.test_user_login_code_error()
    # case02.test_user_login_success()
    
    # 管理员登录
    # login=TestAdminLogin()
    # # case03.test_admin_login_code_error()
    # login.test_admin_login_success()
    # # 添加文章分类
    # # category=TestCategory(login)
    # # category.test_add_category_error()
    # # category.test_add_category_success()
    # # 添加文章
    # article=TestArticle(login)
    # # article.test_add_article()
    # article.test_delete_one_ariticle()
    
    
    pytest.main([r'testcases/log/test_user_login.py'])
    