import sys

import requests
import json
import re
def captchaOCR():
    captcha = ''
    token = ''
    while len(captcha) != 4:
        token = requests.get('https://fangkong.hnu.edu.cn/api/v1/account/getimgvcode').json()['data']['Token']
        headers={}
        data={
            "url":f"https://fangkong.hnu.edu.cn/imagevcode?token={token}",
            "detect_direction":"false"
        }
        headers[b'Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
        resp=requests.post("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=HqsxVsWLZny091CfG2k8EMlM&client_secret=rpIhqY1iKulct7BYxxeHbpcoUKS4bNv7")
        access_token=resp.json()['access_token']
        response=requests.post(f"https://aip.baidubce.com/rest/2.0/ocr/v1/webimage?access_token={access_token}",headers=headers,data=data)
        print(response.json())
        captcha=response.json()['words_result'][0]['words']
    return token, captcha

def login():
    login_url = 'https://fangkong.hnu.edu.cn/api/v1/account/login'
    token, captcha = captchaOCR()
    login_info = {"Code": username, "Password": password, "VerCode": captcha, "Token": token}
    set_cookie = requests.post(login_url, json=login_info).headers['set-cookie']
    print("set_cookie:",set_cookie)
    regex = r"\.ASPXAUTH=(.*?);"
    ASPXAUTH = re.findall(regex, set_cookie)[2]
    print("ASPXAUTH:",ASPXAUTH)

    headers = {'Cookie': f'.ASPXAUTH={ASPXAUTH}; TOKEN={token}'}
    return headers

def main():
    clockin_url = 'https://fangkong.hnu.edu.cn/api/v1/clockinlog/add'
    headers = login()
    clockin_data = {"Temperature": "null",
                    "RealProvince": "湖南省",
                    "RealCity": "长沙市",
                    "RealCounty": "岳麓区",
                    "RealAddress": "宿舍",
                    "IsUnusual": "0",
                    "UnusualInfo": "",
                    "IsTouch": "0",
                    "IsInsulated": "0",
                    "IsSuspected": "0",
                    "IsDiagnosis": "0",
                    "tripinfolist": [
                        {"aTripDate": "", "FromAdr": "", "ToAdr": "", "Number": "", "trippersoninfolist": []}],
                    "toucherinfolist": [],
                    "dailyinfo": {"IsVia": "0", "DateTrip": ""},
                    "IsInCampus": "1",
                    "IsViaHuBei": "0",
                    "IsViaWuHan": "0",
                    "InsulatedAddress": "",
                    "TouchInfo": "",
                    "IsNormalTemperature": "1",
                    "Longitude": 112.925896,
                    "Latitude": 28.238775
                    }
    clockin = requests.post(clockin_url, headers=headers, json=clockin_data)
    print(clockin.text)
    if clockin.status_code == 200:
        if '成功' in clockin.text or '已提交' in clockin.text:
            isSucccess = 0
        else:
            isSucccess = 1
            print(json.loads(clockin.text)['msg'])
    else:
        isSucccess = 1
    print(json.loads(clockin.text)['msg'])
    return isSucccess
if __name__ == '__main__':
    username = "梁原韶"
    password = "哈哈哈"
    if sys.argv[1]:
        username = sys.argv[1]
    if sys.argv[2]:
        password = sys.argv[2]
    main()
