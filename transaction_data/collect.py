import pandas as pd

import requests
from datetime import timedelta, datetime

# 获取中证指数截至前一天每日数据
index = requests.get("https://www.csindex.com.cn/csindex-home/perf/index-perf",
                        params={'indexCode': '931151', 'startDate': '19900101',
                                'endDate': (datetime.today() + timedelta(-1)).strftime('%Y%m%d')}).json().get('data')
print(index)