# coding=utf-8

import scraw
import sms
import uuid
import time
import json
import codecs

#############################################
#得到上一次访问的新闻
#
#
##############################################
def getLastReco():
    f = codecs.open(u'/home/admin/xidian-wxy/lastReco.txt','r+','utf-8')
    recos = f.readlines()
    f.close()
    return recos[0]

def writeLastReco(reco):
    f = codecs.open(u'/home/admin/xidian-wxy/lastReco.txt','w','utf-8')
    f.write(reco)
    f.close()
    
def mainFunc():
    tzgg = (scraw.getTZGG())
    if(tzgg==getLastReco()):
        print(u"没有新消息")
        return
    else:
        writeLastReco(tzgg)
    __business_id = uuid.uuid1()
    print (__business_id)
    #params = "{\"name\":\"张中俊\",\"time\":\"2018/2/1 19:12\"}"
    params={
        "name":u"张中俊",
        "time":"2018/2/1 19:12"
    }

    params["name"] = unicode("xidian-wxy",'utf-8')
    params["time"] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(json.dumps(params))
    res = (sms.send_sms(__business_id, "18792622331", "张中俊", "SMS_123798874", json.dumps(params)))
    if(res["Message"]=="OK"):
        print(u"发送成功")
    else:
        print(u"发送失败")
        print(res)
        
if __name__ == "__main__":
    mainFunc()