# encoding:utf-8
"""
@author: 
@time: 
@desc: 
"""
import requests


class Request:
    def get_method(self, url, data=None, headers=None):
        if not all([url, data, headers]):
            response = requests.get(url, data=data, headers=headers)
        elif headers is not None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url)
        return response

    def post_method(self, url, data=None, headers=None):
        if not all([url, data, headers]):
            response = requests.post(url, data=data, headers=headers)
        elif headers is not None:
            response = requests.post(url, headers=headers)
        else:
            response = requests.post(url)

        return response

    def run(self, method, url, data=None, headers=None):
        response = None
        if method == 'POST':
            response = self.post_method(url, data, headers)
        elif method == 'GET':
            response = self.get_method(url, data, headers)

        return response
