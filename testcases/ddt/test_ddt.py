
import os
from ddt import ddt,data,unpack,file_data
import unittest

def get_data():
    testdata=[{'name':'tom','age':20},{'name':'kite','age':18}]
    return testdata


@ddt
class MyTestCase(unittest.TestCase):
    # 读取元组数据-单租元素
    @data(1,2,3)
    def test1(self,value):
        print(value)
        
    # 读取元组数据-多组元素
    @data((1,2,3),(4,5,6))
    def test2(self,value):
        print(value)
        
        
    # 读取元组数据-拆分元素
    @data((1,2,3),(4,5,6))
    @unpack   # 拆分数据
    def test3(self,value1,value2,value3):
        print(value1,value2,value3)
        
    # 列表
    @data([{'name':'tom','age':20},{'name':'kite','age':18}])    
    def test4(self,value):
        print(value)
        
    # 字典
    @data({'naame':'tom','age':20},{'name':'kite','age':18})
    def test5(self,value):
        print(value)
        
    # 字典-拆分
    @data({'name':'tom','age':20},{'name':'kite','age':18})
    @unpack
    def test6(self,name,age):
        print(name,age)
        
    # 变量或者方法调用
    testdata=[{'name':'tom','age':20},{'name':'kite','age':18}]
    # @data(*testdata)
    @data(get_data())
    def test7(self,value):
        print(value)
        
    #读文件
    @file_data(os.getcwd()+r'/testcases/ddt/test.json')
    def test8(self,value):
        print(value)
        
    
if __name__ == '__main__':
    # unittest.mian()
    unittest.main(argv=['test_ddt.py'], exit=False)
    
    
