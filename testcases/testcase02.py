from time import sleep
import time
from selenium import webdriver
from PIL import Image
import pytesseract
import os


def test1():
    browser=webdriver.Chrome()  
    browser.get('http://192.168.50.5:8080/user/register')
    browser.maximize_window()
    sleep(2)
    # 获取验证码图片
    t=time.time()
    path=os.path.dirname(os.path.dirname(__file__))+'\\screenshots'
    picture_name1=str(t)+'.png'
    browser.save_screenshot(picture_name1)
    
    ce=browser.find_element_by_id('captcha-img')
    left=ce.location['x']
    top=ce.location['y']
    right=ce.size['width']+left
    height=ce.size['height']+top
    im=Image.open(picture_name1)
    # 抠图
    img=im.crop((left,top,right,height))
    t=time.time()
    picture_name2=path+'\\'+str(t)+'.png'
    # 保存二维码图片
    img.save(picture_name2)
    sleep(2)
    browser.close()
    

def test2():
    image1=Image.open('D:\CODE\vscode\selenium_jpress_project\1645368183.765989.png')
    str=pytesseract.image_to_string(image1)
    print(str)
    
 
    
    

    
