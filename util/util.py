from time import sleep
import time
from PIL import Image
import string,random,pickle,os
import ddddocr
import logging
import logging.handlers
import datetime


# 获取验证码图片
def get_code(driver,id):
    t=time.time()
    path=os.path.dirname(os.path.dirname(__file__))+'\\screenshots'
    picture_name1=path+'\\'+str(t)+'.png'
    driver.save_screenshot(picture_name1)
    ce=driver.find_element_by_id(id)
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
    return picture_name2
       
   
# 识别验证码
def identification_verification_code(captcha):
    ocr=ddddocr.DdddOcr()
    with open(captcha,'rb') as file:
        img_bytes=file.read()
    res=ocr.classification(img_bytes)
    captcha=res.split('\n')[-1]
    return captcha
    
    
# 生成随机字符串
def gen_random_str():
    # string.ascii_letters 生成所有字母，string.digits 生成所有数字
    # random.sample的用法，多用于截取列表的指定长度的随机数，但是不会改变列表本身的排序
    rand_str=''.join(random.sample(string.ascii_letters+string.digits,8))
    print('------->',rand_str)
    return rand_str


# 记录日志
def get_logger():
    logger=logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    rf_handler=logging.handlers.TimedRotatingFileHandler(r'logs/all.log',when='midnight',interval=1,backupCount=7,atTime=datetime.time(0,0,0,0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message)s"))

    f_handler=logging.FileHandler(r'logs/error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s[:(lineno)d]-%(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger



# 保存cookie
def save_cookie(driver,path):
    with open(path,'wb') as filehandler:
        cookies=driver.get.cookies()
        print(cookies)
        pickle.dump(cookies,filehandler)
        
        
# 下载cookie
def load_cookie(driver,path):
    with open(path,'rb') as cookiesfile:
        cookies=pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)

