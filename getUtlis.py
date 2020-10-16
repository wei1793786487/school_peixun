import requests
import random

url="http://47.105.237.218:8080/peixun/"
baseHeader = {
    'User-Agent': 'ElectronicLicense/1.4.5 (iPhone; iOS 14.0.1; Scale/3.00)',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': '47.105.237.218:8080',
}

def getCode(phone):
    global baseHeader
    global url
    data = {
        'iphone': phone
    }
    response = requests.post('http://47.105.237.218:8080/peixun/user/getCode', headers=baseHeader, data=data)
    return response.json()

def login(phone):
    global baseHeader
    global url
    data = {
        'code': phone[-6:],
        'iphone': phone
    }
    response = requests.post(url+'/user/longin', headers=baseHeader, data=data)
    return response.json()

def getMyInfo(user_id):
    global baseHeader
    global url
    data = {
        'id': user_id,
    }
    response = requests.post(url+'/user/my', headers=baseHeader, data=data)
    return response.json()


def getSignInfoList(user_id):
    global baseHeader
    global url
    params = (
        ('id', user_id),
        ('pageNum', '1'),
        ('pageSize', '10'),
    )
    response = requests.get(url+'attendance/attendanceList', headers=baseHeader, params=params)
    return response.json()


def getUserInfo(user_id,curriculumId):
    global baseHeader
    global url
    params = (
        ('curriculumId', curriculumId),
        ('id', user_id),
        ('pageNum', '1'),
        ('pageSize', '10'),
    )
    response = requests.get(url+'/attendance/attendanceSignIn', headers=baseHeader,  params=params)
    return response.json()

def sign_in(curriculum_id,type_id,type,lat,log,img_url):
    global baseHeader
    global url
    Score = random.uniform(94, 99)
    params = (
        ('accessKey', 'CfmbXYg5573P5fADMgOuF2RF'),
        ('account', 'zhengxinMGT'),
        ('contrastScore',Score),
        ('curriculumDetailId', curriculum_id),
        ('id', type_id),
        ('img',img_url),
        ('isCheck', '1'),
        ('lat', lat),
        ('log', log),
        ('qiandaoType', '0'),
        ('secretKey', 'B5Y1MmCLdKg8xce2bSfHusrjTc4kyN6V'),
        ('type', type),
    )
    response = requests.get(url+'/curriculum/signIn', headers=baseHeader, params=params)
    return  response.json()