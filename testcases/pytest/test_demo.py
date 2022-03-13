import pytest

class TestLoginCase(object):
    
    def test01(self):
        print('------test01-------')
        
    def test02(self):
        print('-----------test02-------------')
        assert 1<22
        
        
        
if __name__ == '__main__':
    pytest.main(['-sv',r'./testcases/pytest/test_demo.py'])
    