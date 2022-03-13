from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TestCategory(object):
    def __init__(self,login):
        self.login=login
        

    # 测试文章分类失败，名称为空的场景
    def test_add_category_error(self):
        name=''
        parent='Python'
        slug='test'
        excepted='这是必填内容'
        
        # 点击文章 
        self.login.driver.find_element_by_id('article').click()
        sleep(1)
        # 点击分类 
        self.login.driver.find_element_by_xpath('//*[@id="分类--/admin/article/category"]').click()
        # 输入分类名称
        self.login.driver.find_element_by_name('category.title').send_keys(name)
        # 选择父分类,先定位到下拉框
        parent_category_elem=self.login.driver.find_element_by_name('category.pid')
        # 根据选项内容定位
        Select(parent_category_elem).select_by_visible_text(parent)
        # 输入固定链接category.slug
        self.login.driver.find_element_by_name('category.slug').send_keys(slug)
        # 点击提交按钮 
        self.login.driver.find_element_by_class_name('btn').click()
        
        WebDriverWait(self.login.driver,5).until(EC.text_to_be_present_in_element((By.ID,'category.title-error'),excepted))   
        print('----->执行成功')
        sleep(2)
            
            
    # 测试文章分类成功    
    def test_add_category_success(self):
        name='test'        
        parent='Python'
        slug='测试相关'
        
            # 点击文章 
        self.login.driver.find_element_by_id('article').click()
        sleep(1)
        # 点击分类 
        self.login.driver.find_element_by_xpath('//*[@id="分类--/admin/article/category"]').click()
        # 输入分类名称
        self.login.driver.find_element_by_name('category.title').clear()
        self.login.driver.find_element_by_name('category.title').send_keys(name)
        # 选择父分类,先定位到下拉框
        parent_category_elem=self.login.driver.find_element_by_name('category.pid')
        # 根据选项内容定位
        Select(parent_category_elem).select_by_visible_text(parent)
        # 输入固定链接category.slug
        self.login.driver.find_element_by_name('category.slug').clear()
        self.login.driver.find_element_by_name('category.slug').send_keys(slug)
        # 点击提交按钮 
        self.login.driver.find_element_by_class_name('btn').click()
        sleep(3)
        self.login.driver.quit()
        
            
            
    