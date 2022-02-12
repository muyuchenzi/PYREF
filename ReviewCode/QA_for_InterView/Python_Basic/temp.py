# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json
import requests
def test():

    appid = '20220212001080952'  # 填写你的appid
    secretKey = '7hmzzpojDNLIdUD5M'  # 填写你的密钥

    httpClient = None
    myurl = 'http://api/trans/vip/translate'

    fromLang = 'en'   #原文语种
    toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    q= 'test'
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl =myurl + '?q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang +'&appid=' + appid+ '&salt=' + str(salt) + '&sign=' + sign
    # text=requests.get(myurl)
    # print(text)
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        print (result)

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()

test()


def temp():

    ss=hashlib.md5()