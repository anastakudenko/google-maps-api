from pickle import GET

import requests

from utils.logger import Logger

"""Список http методов"""


class HttpMethod:
    headers = {'Content-Type': 'application/json'}
    cookies = ''

    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=HttpMethod.headers, cookies=HttpMethod.cookies)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookies)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookies)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookies)
        return result
