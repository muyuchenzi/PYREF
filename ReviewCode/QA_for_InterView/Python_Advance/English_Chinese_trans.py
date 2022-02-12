import http.client
import hashlib
import urllib
import random
import json
import requests
def post_to_baidu(from_text,to_text,input_text):
    '''
    APP ID：20220212001080952

    密钥：7hmzzpojDNLIdUD5MkUb
  
    '''
    appid="20220212001080952"
    secretKey='7hmzzpojDNLIdUD5MkUb'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    fromLang=from_text
    toLang=to_text
    salt=random.randint(32768, 65536)
    q=input_text
    sign=appid+q+str(salt)+secretKey
    sign=hashlib.md5(sign.encode()).hexdigest()
    #配置字段结束
    my_url=myurl+ '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' +\
         fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    # NOTE 第一种方法
    trans_url='http://api.fanyi.baidu.com/api/trans/vip/translate'
    params={
        'q':input_text,
        'from':from_text,
        'to':to_text,
        'appid':appid,
        'salt':salt,
        'sign':sign
    }
    try:
        response=requests.get(trans_url,params=params)
        result_dict=response.json()
        if 'trans_result' in result_dict:
            return result_dict['trans_result'][0]['src'],result_dict['trans_result'][0]['dst']
        else:
            print('Some error occured: ',result_dict)
    except Exception as e:
        print('访问失败！')
#    NOTE 第二种方法 访问失败，不建议尝试。
    # try:
    #     httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    #     httpClient.request('Get', my_url)

    #     # response是HTTPResponse对象
    #     response = httpClient.getresponse()
    #     result_all = response.read().decode("utf-8")
    #     result = json.loads(result_all)

    #     print (result)

    # except Exception as e:
    #     print (e)
    # finally:
    #     if httpClient:
    #         httpClient.close()

def chinese_or_english(input_text):
    from_text=''
    to_text=""
    for word in input_text:
        if   '\u4e00'<=word<='\u9fff':
            from_text='zh' 
            to_text="en"
        else:
            from_text='en'
            to_text="zh"
    return from_text,to_text


def func_entry():
    entry_text=input("请输入需要翻译的句子:")
    from_text,to_text=chinese_or_english(input_text=entry_text.strip())
    from_result,to_result=post_to_baidu(from_text,to_text,entry_text)
    print(from_result,to_result)


if __name__=="__main__":
    func_entry()