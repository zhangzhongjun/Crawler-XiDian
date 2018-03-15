# coding=utf-8
import requests
# -*- coding: utf-8 -*-
import codecs
import os.path
import os
from bs4 import BeautifulSoup

import time
url = 'http://gr.xidian.edu.cn/'
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
    data = soup.find("ul",class_="dongtai-list")
    data = data.find("li").find("a").text
    return data
    
if __name__=="__main__":
    print(getTZGG())