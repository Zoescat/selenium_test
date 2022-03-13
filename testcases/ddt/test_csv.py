import csv
import pytest

def get_data():
    with open(r'testcases/ddt/test.csv')as f:
        lst=csv.reader(f)
        my_data=[]
        for row in lst:
            my_data.extend(row)
        return my_data
    
    
@pytest.mark.parametrize('name',get_data())
def test_name(name):
    print(name)
    
    
if __name__ == '__main__':
    # print(get_data())
    pytest.main(['-sv',r'testcases/ddt/test_csv.py'])
    