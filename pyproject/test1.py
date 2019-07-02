from selenium import webdriver
import random
import sys
from sql import  Mysql
from datetime import *
import selenium
from Linux import *
# cpu()


from selenium.webdriver.support.select import Select


# driver=webdriver.Chrome()
# driver=driver.get('https://www.baidu.com')
# a=datetime.now()
# print(a.date())
def random_num(num):#返回指定位数的随机数字字符串
    id = ''.join(str(i) for i in random.sample(range(0, 9), num))  # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
    return id

def read_isspace(dir): #有空格的文本处理，返回逗号分隔的数组
    file = open(dir)
    # 按行读取
    contents = file.readlines()
    # 数组
    arr = []
    for item in contents:
        # 清除换行、空格
        content = item.strip()
       # print(content)
        p = ','.join(content.split())
        # 按照","分割
        #temp = content.split(",")
        temp = p.split(",")
        arr.append(temp)
    return arr
def read_douhao(dir):#有逗号的文本处理，重新组成数组
    file = open(dir)
    # 按行读取
    contents = file.readlines()
    # 数组
    arr = []
    for item in contents:
        # 清除换行、空格
        content = item.strip()
        temp = content.split(",")
        arr.append(temp)
        print('aaaaaaa')
    return arr
