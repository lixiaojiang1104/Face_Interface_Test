# encoding:utf-8
"""
@author: 
@time: 
@desc: 生成随机数
"""
import time
import pytz
import random
from datetime import datetime


def random_signature_nonce():
    """
    随机生成signature_nonce
    :return:
    """
    init_nonce = ''
    for i in range(14):
        random_str = chr(random.randrange(ord('0'), ord('9') + 1))
        init_nonce += random_str
    return init_nonce


def generate_signature():
    """
    生成Signature值
    :return:
    """
    pass
    # "http://imm.cn-shanghai.aliyuncs.com/?Project%3dtest-project%26RegionId%3dcn-shanghai%26AccessKeyId%3dtestid%26Format%3dJSON%26SignatureMethod%3dHMAC-SHA1%26SignatureVersion%3d1.0%26SignatureNonce%3dd1ac7371108dc53541c9d0f29e5396c7%26Timestamp%3d2019-02-22T09%253A30%253A54Z%26Action%3dGetProject%26Version%3d2017-09-06"
    # "http://imm.cn-shanghai.aliyuncs.com/?Project=test-project&RegionId=cn-shanghai&AccessKeyId=testid&Format=JSON&SignatureMethod=HMAC-SHA1&SignatureVersion=1.0&SignatureNonce=d1ac7371108dc53541c9d0f29e5396c7&Timestamp=2019-02-22T09%3A30%3A54Z&Action=GetProject&Version=2017-09-06Signature=NPzJnV5HAdj4jkShTWKa9WwOZxU%3D"


def generate_utc_time_now():
    """
    生成UTC时间
    :return:
    """
    # return datetime.now().__format__("%Y-%m-%d %H:%M:%S")
    utc_time = datetime.now(tz=pytz.timezone('UTC')).isoformat()
    utc_time = utc_time.split('.')[0] + 'Z'
    return utc_time


def generate_time_now():
    """
    生成当前时间
    :return:
    """
    return datetime.now().__format__("%Y-%m-%d %H:%M:%S")
    # utc_time = datetime.now(tz=pytz.timezone('UTC')).isoformat()
    # utc_time = utc_time.split('.')[0] + 'Z'
    # print(utc_time)
    # return utc_time


# print(generate_time_now())
