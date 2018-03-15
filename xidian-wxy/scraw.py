# coding=utf-8
import requests
# -*- coding: utf-8 -*-
import codecs
import os.path
import os
from bs4 import BeautifulSoup

import time
url = 'http://ce.xidian.edu.cn/tzgg.htm'
import json
header = {

}
parameter = {

}

def getTZGG():
    res = requests.get(url,params = parameter,headers=header,timeout=10,auth=False)
    while res.status_code!=200:
        print (str(res)+'retrying...')
        res = requests.get(url,params = parameter,headers=header,timeout=50)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    data = soup.find("li",id="line_u6_0")
    data = data.find("a").text
    return data
    
if __name__=="__main__":
    print(getTZGG())