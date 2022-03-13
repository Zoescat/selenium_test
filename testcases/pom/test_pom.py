
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

class BaiduPage(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        
        self.input_element=(By.ID,'kw')
        self.btn_element=(By.ID,'su')
        
    def goto_baidu(self,url):
        self.driver.get(url)
        
    def search(self,url,kw):
        self.goto_baidu(url)
        self.driver.find_element(*self.input_element).send_keys(kw)
        self.driver.find_element(*self.btn_element).click()
        sleep(5)
    
class TestBaidu(unittest.TestCase):
    def setUp(self) -> None:
        self.baiduPage=BaiduPage()
        
    def test_search(self):
        self.baiduPage.search('http://www.baidu.com','selenium')
        
        
if __name__ == '__main__':
    unittest.main(argv=['test_pom.py'], exit=False)
    