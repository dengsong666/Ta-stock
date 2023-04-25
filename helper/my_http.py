import time

import requests
from fake_useragent import UserAgent

ua = UserAgent()


def ph():
    proxy = requests.get("http://127.0.0.1:5010/get").json().get("proxy")
    proxies = {"http": "http://{}".format(proxy)}
    headers = {
        "User-Agent": ua.random,

    }
    return proxies, headers, proxy


def crawler(url, params, retry_count=10):
    proxies, headers, proxy = ph()
    while retry_count > 0:
        try:
            print(url, params, proxies, headers)
            # 使用代理访问
            v = requests.get(url, params=params, proxies=proxies, headers=headers).json().get('data')
            if not v: raise Exception()
            return v
        except Exception:
            retry_count -= 1
            print(retry_count)
            if not retry_count % 2:
                requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
                proxies, headers, proxy = ph()
    # 删除代理池中代理
    # requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
    return None
