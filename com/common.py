import requests
from com.logger import logger


class TestCom(object):
    base_url = 'https://iot.hzlitiot.com'

    @classmethod
    def setup_class(cls):
        login_url = cls.base_url + '/api/security/oauth/token'
        login_data = {
            'username': 'super',
            'password': 'super2020',
            'grant_type': 'password',
            'client_id': 'd53a7258-9494-4ef4-b755-2e4d4a8d453c',
            'client_secret': '123456'
        }
        r = requests.post(url=login_url, data=login_data)
        cls.token = r.json()['access_token']

    @classmethod
    def request(self, method: str, url, params=None, data=None, json=None, **kwargs):
        method = method.upper()
        if method == "GET":
            res = requests.get(url, params=params, **kwargs)
            logger.info(f"请求方法：{method}，请求地址：{url}，请求参数：{res.request.body}，响应结果：{res.text}")
            return res
        elif method == "POST":
            res = requests.post(url, data=data, json=json, **kwargs)
            logger.info(f"请求方法：{method}，请求地址：{url}，请求参数：{res.request.body}，响应结果：{res.text}")
            return res
        else:
            print("请求方法未定义，请检查！")
