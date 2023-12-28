import requests
import time
import json
import os

token = os.environ.get('cfn')

def lookVideo():
    url = 'http://cfn.tuesjf.cn/apis/v1/lookVideo'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/105/YM-RT/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://m.cfn.tuesjf.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = {
        'look_type': '1',
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    msg = result['msg']
    print(f"观看结果:{msg}")
    time.sleep(15)

def receiveVideo():
    print(">>>>>开始领取收益<<<<<")
    url = 'http://cfn.tuesjf.cn/apis/v1/receiveVideo'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/105/YM-RT/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://m.cfn.tuesjf.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = {
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    msg = result['msg']
    print(f"领取结果:{msg}")

def cachSave():
    print(">>>>>开始提现<<<<<")
    url = "http://cfn.tuesjf.cn/apis/v1/cachSave"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/105/YM-RT/",
        "content-type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "http://m.cfn.tuesjf.cn",
        "X-Requested-With": "com.hjtq",
        "Referer": "http://m.cfn.tuesjf.cn/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {
        "id": "3",
        "token": token
    }  
    response = requests.post(url, headers=headers, data=data)
    response_data = response.text
    data = json.loads(response_data)
    msg = data["msg"]
    if msg == "提现成功":
        print("提现成功")
    else:
        print("已提现")

if __name__ == "__main__":
    while True:
        lookVideo()
        receiveVideo()
        cachSave()