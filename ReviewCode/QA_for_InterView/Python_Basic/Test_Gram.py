import hashlib
import random

appid = '20220212001080952'
secretKey = '7hmzzpojDNLIdUD5M'  # 填写你的密钥
myurl = 'api.fanyi.baidu.com/api/trans/vip/translate'
q = 'test'
salt = random.randint(2333332, 3333332)
from_text = "en"
to_text = "zh"
sign_b = appid + q + str(1435660288) + secretKey
sign = hashlib.md5(sign_b.encode()).hexdigest()

url = myurl + "?q=" + q + "&from=" + from_text + "&to=" + to_text + "&appid=" + appid + "&salt=" + str(
    1435660288) + "&sign=" + sign
print(url)
q = 'test &from=en & to = zh & appid = 20220212001080952 & salt = 1435660288 & sign = 37302803335333c3162c772373cc35e0'
x = 'q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4'
y = 'q=test&from=en&to=zh&appid=20220212001080952&salt=1435660288&sign=37302803335333c3162c772373cc35e0'
