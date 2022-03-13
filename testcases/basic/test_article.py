from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class TestArticle(object):
    def __init__(self,login): 
        self.login=login
        
    # 测试添加文章
    def test_add_article(self):
        article_title='我的文章标题'
        content='文章内容'
        excepted='文章保存成功。'
        
        # 点击文章
        self.login.driver.find_element_by_id('article').click()
        sleep(1)
        # 点击写文章
        self.login.driver.find_element_by_xpath('//*[@id="写文章--/admin/article/write"]/a').click()
        sleep(1)
        
        # 定位到文章标题
        self.login.driver.find_element_by_xpath('//*[@id="article-title"]').send_keys(article_title)
        # self.login.driver.find_element_by_css_selector('#article-title').send_keys(article_title)
        js="document.querySelector('#form > div > div.col-lg-9 > div > div:nth-child(2) > div:nth-child(2) > div.ck.ck-reset.ck-editor.ck-rounded-corners > div.ck.ck-editor__main > div > p').innerText='哈哈哈哈哈😄'"
        self.login.driver.execute_script(js)
        # 点击发布按钮
        self.login.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()
        
        # 断言
        WebDriverWait(self.login.driver,5).until(EC.text_to_be_present_in_element((By.CLASS_NAME,'toast-message'),excepted))  
        print('-----over!!!')
        
        
    # 删除单个文章  //*[@id="文章管理--/admin/article/list"]/a
    def test_delete_one_ariticle(self):
        self.login.driver.find_element_by_id('article').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="文章管理--/admin/article/list"]').click()
        sleep(1)
        # 
        link = self.login.driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div/div[2]/table/tbody/tr[1]')
        ActionChains(self.login.driver).move_to_element(link).perform()
        sleep(1)
         # 测试前文章数 共 3 条
        con1=self.login.driver.find_element_by_class_name('pagination-total-text').text[2]

        # 点击删除
        del_elem = self.login.driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/div/div/a[2]')
        del_elem.click()
        sleep(1)
        # 删除后的文章数  
        con2=self.login.driver.find_element_by_class_name('pagination-total-text').text[2]
        print('-------->',con1,con2)
        assert int(con1) == int(con2) + 1
        print('---成功了！！！')
        
        
        