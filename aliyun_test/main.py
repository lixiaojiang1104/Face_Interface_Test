# encoding:utf-8
"""
@author: 
@time: 
@desc: 主程序
"""
import settings
from data_processing.get_data import GetData
from data_processing.send_email import SendEmail
from utils.help import generate_utc_time_now, random_signature_nonce, generate_time_now
from utils.request import Request


class Run:
    def __init__(self):
        self.request = Request()
        self.get_data = GetData()
        self.param = self.params_all()

    def params_all(self):
        """构造请求参数"""
        params = settings.PARAMS_ALL
        params['Timestamp'] = str(generate_utc_time_now())
        params['SignatureNonce'] = random_signature_nonce()
        params['Project'] = "aliyun_test"
        return params

    def splice_request_url(self, url, url_key):
        """拼接请求url"""
        request_url = None
        if url_key == "params_all_url":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"], ImageUri=self.param["ImageUri"],
                                     Timestamp=self.param["Timestamp"])
        elif url_key == "must_params_url":
            request_url = url.format(Version=self.param["Version"], AccessKeyId=self.param["AccessKeyId"], Signature=self.param["Signature"],
                                     SignatureMethod=self.param["SignatureMethod"], Timestamp=self.param["Timestamp"], SignatureVersion=self.param["SignatureVersion"],
                                     SignatureNonce=self.param["SignatureNonce"], Project=self.param["Project"], ImageUri=self.param["ImageUri"])
        elif url_key == "lost_must_params_url":
            parms = settings.LOST_MUST_PARAMS
            request_url = url.format(Version=parms["Version"], AccessKeyId=parms["AccessKeyId"], Signature=parms["Signature"],
                                     SignatureMethod=parms["SignatureMethod"], Timestamp=parms["Timestamp"], SignatureVersion=parms["SignatureVersion"],
                                     SignatureNonce=parms["SignatureNonce"], Project=parms["Project"], ImageUri=parms["ImageUri"])
        elif url_key == "error_version_params_url_01":
            request_url = url.format(Format=self.param['Format'], Version=settings.VERSION_ERROR_PARAMS['Version_01'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"], ImageUri=self.param["ImageUri"],
                                     Timestamp=self.param["Timestamp"])
        elif url_key == "error_version_params_url_02":
            request_url = url.format(Format=self.param['Format'], Version=settings.VERSION_ERROR_PARAMS['Version_02'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"], ImageUri=self.param["ImageUri"],
                                     Timestamp=self.param["Timestamp"])
        elif url_key == "error_version_params_url_03":
            request_url = url.format(Format=self.param['Format'], Version=settings.VERSION_ERROR_PARAMS['Version_03'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"], ImageUri=self.param["ImageUri"],
                                     Timestamp=self.param["Timestamp"])
        elif url_key == "error_version_params_url_04":
            request_url = url.format(Format=self.param['Format'], Version=settings.VERSION_ERROR_PARAMS['Version_04'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"], ImageUri=self.param["ImageUri"],
                                     Timestamp=self.param["Timestamp"])
        elif url_key == "error_version_params_url_05":
            request_url = url.format(Format=self.param['Format'], Version=settings.VERSION_ERROR_PARAMS['Version_05'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"], ImageUri=self.param["ImageUri"],
                                     Timestamp=self.param["Timestamp"])
        elif url_key == "error_accesskeyid_params_url_01":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=settings.AccessKeyId_ERROR_PARAMS["AccessKeyId_01"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"], ImageUri=self.param["ImageUri"],
                                     Timestamp=self.param["Timestamp"])
        elif url_key == "error_accesskeyid_params_url_02":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=settings.AccessKeyId_ERROR_PARAMS["AccessKeyId_02"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"], ImageUri=self.param["ImageUri"],
                                     Timestamp=self.param["Timestamp"])
        elif url_key == "error_accesskeyid_params_url_03":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=settings.AccessKeyId_ERROR_PARAMS["AccessKeyId_03"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"], ImageUri=self.param["ImageUri"],
                                     Timestamp=self.param["Timestamp"])
        elif url_key == "error_signaturemethod_params_url_01":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=settings.SignatureMethod_ERROR_PARAMS["SignatureMethod_01"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"], ImageUri=self.param["ImageUri"],
                                     Timestamp=self.param["Timestamp"])
        elif url_key == "error_timestamp_params_url_01":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"], ImageUri=self.param["ImageUri"],
                                     Timestamp=generate_time_now())
        elif url_key == "error_SignatureNonce_params_url_01":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"],
                                     SignatureNonce=settings.SignatureNonce_ERROR_PARAMS["SignatureNonce_01"], SignatureVersion=self.param["SignatureVersion"],
                                     Project=self.param["Project"], ImageUri=self.param["ImageUri"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_SignatureNonce_params_url_02":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"],
                                     SignatureNonce=settings.SignatureNonce_ERROR_PARAMS["SignatureNonce_02"], SignatureVersion=self.param["SignatureVersion"],
                                     Project=self.param["Project"], ImageUri=self.param["ImageUri"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_SignatureNonce_params_url_03":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"],
                                     SignatureNonce=settings.SignatureNonce_ERROR_PARAMS["SignatureNonce_03"], SignatureVersion=self.param["SignatureVersion"],
                                     Project=self.param["Project"], ImageUri=self.param["ImageUri"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_SignatureNonce_params_url_04":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"],
                                     SignatureNonce=settings.SignatureNonce_ERROR_PARAMS["SignatureNonce_04"], SignatureVersion=self.param["SignatureVersion"],
                                     Project=self.param["Project"], ImageUri=self.param["ImageUri"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_signatureversion_01_params_url_01":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"],
                                     SignatureNonce=self.param["SignatureNonce"], SignatureVersion=settings.SignatureVersion_ERROR_PARAMS["SignatureVersion_01"],
                                     Project=self.param["Project"], ImageUri=self.param["ImageUri"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_signatureversion_01_params_url_02":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"],
                                     SignatureNonce=self.param["SignatureNonce"], SignatureVersion=settings.SignatureVersion_ERROR_PARAMS["SignatureVersion_02"],
                                     Project=self.param["Project"], ImageUri=self.param["ImageUri"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_signatureversion_01_params_url_03":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"],
                                     SignatureNonce=self.param["SignatureNonce"], SignatureVersion=settings.SignatureVersion_ERROR_PARAMS["SignatureVersion_03"],
                                     Project=self.param["Project"], ImageUri=self.param["ImageUri"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_signatureversion_01_params_url_04":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"],
                                     SignatureNonce=self.param["SignatureNonce"], SignatureVersion=settings.SignatureVersion_ERROR_PARAMS["SignatureVersion_04"],
                                     Project=self.param["Project"], ImageUri=self.param["ImageUri"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_project_params_url_01":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"],
                                     SignatureNonce=self.param["SignatureNonce"], SignatureVersion=self.param["SignatureNonce"],
                                     Project=settings.Project_ERROR_PARAMS["Project_01"], ImageUri=self.param["ImageUri"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_project_params_url_02":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"],
                                     SignatureNonce=self.param["SignatureNonce"], SignatureVersion=self.param["SignatureNonce"],
                                     Project=settings.Project_ERROR_PARAMS["Project_02"], ImageUri=self.param["ImageUri"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_project_params_url_03":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"],
                                     SignatureNonce=self.param["SignatureNonce"], SignatureVersion=self.param["SignatureNonce"],
                                     Project=settings.Project_ERROR_PARAMS["Project_03"], ImageUri=self.param["ImageUri"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_ImageUri_params_url_01":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"],
                                     ImageUri=settings.ImageUri_ERROR_PARAMS["ImageUri_01"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_ImageUri_params_url_02":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"],
                                     ImageUri=settings.ImageUri_ERROR_PARAMS["ImageUri_02"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_ImageUri_params_url_03":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"],
                                     ImageUri=settings.ImageUri_ERROR_PARAMS["ImageUri_03"], Timestamp=self.param["Timestamp"])
        elif url_key == "error_ImageUri_params_url_04":
            request_url = url.format(Format=self.param['Format'], Version=self.param['Version'], AccessKeyId=self.param["AccessKeyId"],
                                     Signature=self.param["Signature"], SignatureMethod=self.param["SignatureMethod"], SignatureNonce=self.param["SignatureNonce"],
                                     SignatureVersion=self.param["SignatureVersion"], Project=self.param["Project"],
                                     ImageUri=settings.ImageUri_ERROR_PARAMS["ImageUri_04"], Timestamp=self.param["Timestamp"])
        return request_url

    def running(self):
        rows = self.get_data.excel_lines()
        for row in range(1, rows):
            is_run = self.get_data.get_is_run(row)
            url, url_key = self.get_data.get_request_url(row)
            url = self.splice_request_url(url, url_key)

            method = self.get_data.get_request_method(row)
            if not is_run:
                continue
            if not url:
                continue
            response = self.request.run(method, url)
            print("%s, response: %s" % (url_key, response))
            if response.status_code != 200:
                result = "fail"
            else:
                result = "success"
            self.get_data.write_result(row, result)

if __name__ == '__main__':
    run = Run()
    run.running()
    SendEmail(settings.fromaddr,settings.password,settings.toaddrs).send_email()
