# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re

url = 'http://10.255.44.33/srun_portal_pc.php'
header = {

}
parameter = {

}
data = {
    'action':'login',
    'ac_id':'1',
    'user_ip':'',
    'nas_ip':'',
    'user_mac':'',
    'url':'',
    'username':'这里是学号',
    'password':'这里是密码'
}

def getTZGG():
    res = requests.post(url,data=data,headers=header,timeout=10,auth=False)
    while res.status_code!=200:
        print (str(res)+'retrying...')
        res = requests.post(url,data=data,headers=header,timeout=50,auth=False)
    res.encoding = 'utf-8'
    try{
        soup = BeautifulSoup(res.text,'html.parser')
        user_name = soup.find("span",id="user_name").text
        user_ip = soup.find("script",text=re.compile(r'setTimeout')).text
        user_ip = user_ip[user_ip.find("'")+1:user_ip.rfind("'"):1]
        return {"user_name":user_name,"user_ip":user_ip}
    }catch(Exception e){
        return "获取信息时候出错，不过应该已经连接上了。。。"
    }
if __name__=="__main__":
    print(getTZGG())