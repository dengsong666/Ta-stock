import time

import pandas as pd

import requests

"""
swindexcode: 指数代码
bargaindate: 发布日期
openindex:开盘指数
maxindex: 最高指数
minindex: 最低指数
closeindex: 收盘指数 
hike: 未知
markup:涨跌幅
bargainamount: 成交量
bargainsum: 成交额
"""
start = time.perf_counter()
industry = requests.get("https://www.swsresearch.com/institute-sw/api/index_name/", params={'indextype': '二级行业'})
for item in industry.json().get('data'):
    day = requests.get("https://www.swsresearch.com/institute-sw/api/index_publish/trend/",
                       params={'swindexcode': item['swindexcode'], 'period': 'DAY'})
    df = pd.DataFrame(day.json().get('data')).drop(columns=['swindexcode', 'hike'], errors='ignore')
    print(df.iloc[-1:])
    # df.to_csv(item['swindexname'] + '-' + item['swindexcode'] + ".csv", index=False, sep=',')

print(f'{time.perf_counter()-start}s')