''' 
@阿慈
垃圾毛自己玩吧
入口：https://wx.qrurl.net/?t=231005dD57Uv
new Env('垃圾毛'); 
www.rroadem.cn域名内的session_id末尾的scene填入变量
'''
import os
import requests

qtjt_data = os.getenv('qtjt').split('@')

headers = {
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a2a) NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wxf2b0ee8ed60663b4/6/page-frame.html'
}

data = {
    "hid": "30"
}

for i in range(len(qtjt_data)):
    qtjt_params = qtjt_data[i].split('&')
    
    session_id = qtjt_params[0]
    scene = qtjt_params[1]
    
    url = f"https://www.rroadem.cn/?s=/ApiRewardVideoAd/givereward&aid=3&platform=wx&session_id={session_id}&pid=0&scene={scene}"
    
    response = requests.post(url, headers=headers, json=data)
    json_data = response.json()
    
    msg = json_data.get('msg')
    print(f"第{i+1}个号运行结果：{msg}")
