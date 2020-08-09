import pytest
import allure
import os


def test_1():
    print("这是allure")
    assert 0 == 0

if __name__ == '__main__':
    pytest.main(['-sv','yy.py','--alluredir=repote'])
    #os.system('allure serve repote')