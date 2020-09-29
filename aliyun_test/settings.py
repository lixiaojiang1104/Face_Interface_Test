# encoding:utf-8
"""
@author: 
@time: 
@desc: 
"""

fromaddr = '1434749028@qq.com'
password = 'xxxxxx'
toaddrs = ['xxx@126.com','xxx@163.com']

PROJECT_PATH = "D:/pycharm/aliyun_test/"
ALIYUN_CASE_FILE_PATH = PROJECT_PATH + "data/aliyun_test_case.xlsx"
ALIYUN_CASE_FILE_SHEET_NAME_1 = "Sheet1"
ALIYUN_CASE_FILE_SHEET_INDEX_1 = 0
dict_col_name = {
    "test_module" : 0,
    "case_id" : 1,
    "case_name" : 2,
    "method" : 3,
    "request_url" : 4,
    "whether" : 5,
    "header" : 6,
    "test_data" : 7,
    "test_procedure" : 8,
    "expected_result" : 9,
    "real_result" : 10,
    "priority" : 11,
    "importance" : 12,
    "whether_will_now" : 13,
    "depend_id" : 14,
    "depend_data" : 15,
    "depend_key" : 16,
    "is_run" : 17
}

AccessKeyId = 'LTAI4FhttccgzPWZMCGqu2N3'
AccessKeySecret = 'ZrfC6UkChDnej7EoTfcgXGKsTRgZbQ'

PARAMS_ALL = {
    "Format": "json",
    "Version": "2017-09-06",
    "AccessKeyId": AccessKeyId,
    "Signature": "",
    "SignatureMethod": "HMAC-SHA1",
    "SignatureNonce": "",
    "SignatureVersion": "1.0",
    "Project": "",
    "ImageUri": "oss://imm-test/testcases/test.jpg",
    "Timestamp": ""
}

MUST_PARAMS = {
    "Version": None,
    "AccessKeyId": AccessKeyId,
    "Signature": "",
    "SignatureMethod": None,
    "SignatureNonce": "",
    "SignatureVersion": "1.0",
    "Project": "",
    "ImageUri": "",
    "Timestamp": ""
}

LOST_MUST_PARAMS = {
    "Version": None,
    "AccessKeyId": AccessKeyId,
    "Signature": "",
    "SignatureMethod": None,
    "SignatureNonce": "",
    "SignatureVersion": "1.0",
    "Project": "",
    "ImageUri": "oss://imm-test/testcases/test.jpg",
    "Timestamp": ""
}

VERSION_ERROR_PARAMS = {
    "Version_01": "2017 09 06",
    "Version_02": "2017_09_06",
    "Version_03": "20170906",
    "Version_04": "201796",
    "Version_05": "2017-9-06",
}

AccessKeyId_ERROR_PARAMS = {
    "AccessKeyId_01" : "2017-9-06LTAI4FhttccgzPWZMCG@#$%^",
    "AccessKeyId_02" : "LTAI4FhttccgzPWZMCGqu2N3LTAI4FhttccgzPWZMCGqu2N3LTAI4FhttccgzPWZMCGqu2N3LTAI4FhttccgzPWZMCGqu2N3LTAI4FhttccgzPWZMCGqu2N3LTAI4FhttccgzPWZMCGqu2N3",
    "AccessKeyId_03" : "L"
}

SignatureMethod_ERROR_PARAMS = {
    "SignatureMethod_01" : "HMAC-SHA1999"
}

Signature_ERROR_PARAMS = {
    "Signature_01": ""
}

SignatureNonce_ERROR_PARAMS = {
    "SignatureNonce_01": "1234567890098",
    "SignatureNonce_02": "123456789009876",
    "SignatureNonce_03" : "1234567890@#$%",
    "SignatureNonce_04" : "1234567890abcd"
}

SignatureVersion_ERROR_PARAMS = {
    "SignatureVersion_01": "0.0",
    "SignatureVersion_02": "a.b",
    "SignatureVersion_03" : "1.0#$",
    "SignatureVersion_04" : "100.192.0.101.56.89.354.234.88.97.79.08.56.47.34.56.36.83.25.26.38.45.6.37.48.356.74.84.24.467.234.56"
}

Project_ERROR_PARAMS = {
    "Project_01": "test",
    "Project_02" : "test@#$",
    "Project_03": "aliyun_test_aliyun_test_aliyun_test_aliyun_test_aliyun_test_aliyun_test_aliyun_test_aliyun_test_aliyun_test_aliyun_test"
}

Timestamp_ERROR_PARAMS = {
    "Timestamp_01": ""
}

ImageUri_ERROR_PARAMS = {
    "ImageUri_01": "oss://imm-test/testcases/test.png",
    "ImageUri_02": "oss://imm-test/testcases/test.jpeg",
    "ImageUri_03": "oss://imm-test/testcases/test.gif",
    "ImageUri_04": "oss://imm-test/testcases/test.bmp",
}