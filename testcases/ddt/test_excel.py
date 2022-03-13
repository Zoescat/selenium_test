
import pytest
import xlrd

def get_data():
    filename=r'testcases/ddt/data.xlsx'
    wb=xlrd.open_workbook(filename)
    sheet=wb.sheet_by_index(0)
    rows=sheet.nrows
    cols=sheet.ncols
    lst=[]
    for row in range(rows):
        for col in range(cols):
            cell_data=sheet.cell_value(row,col)
            lst.append(cell_data)
    return lst

@pytest.mark.parametrize('name',get_data())        
def test_name(name):
    print(name)
    
    
if __name__ == '__main__':
    pytest.main(['-sv',r'testcases/ddt/test_excel.py'])
    
    