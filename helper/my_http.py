import requests
from fake_useragent import UserAgent

ua = UserAgent()


def crawler(url, params, retry_count=5):
    proxy = requests.get("http://127.0.0.1:5010/get").json().get("proxy")
    proxies = {"http": "http://{}".format(proxy)}
    headers = {"User-Agent": ua.random}
    print(url, params, proxies, headers)
    while retry_count > 0:
        try:
            # 使用代理访问
            v = requests.get(url, params=params, proxies=proxies, headers=headers).json().get('data')
            # print(v)
            return v
        except Exception:
            retry_count -= 1
    # 删除代理池中代理
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
    return None
