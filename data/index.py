import os
import pandas as pd
import requests
from datetime import timedelta, datetime

# 获取中证指数截至前一天每日数据
def save_day(code, name, start_date='19900101', end_date=(datetime.today() + timedelta(-1)).strftime('%Y%m%d')):
    filename = f"中证指数/{name}-{code}.csv"
    mode = 'w'
    header = True
    if os.path.exists(filename) and os.path.getsize(filename):
        mode = 'a'
        header = False
        last_date = pd.read_csv(filename).tail(1)['tradeDate'].reset_index(drop=True)[0]
        start_date = (datetime.strptime(f'{last_date}', "%Y%m%d") + timedelta(1)).strftime('%Y%m%d')
    api = "https://www.csindex.com.cn/csindex-home/perf/index-perf"
    params = {'indexCode': code, 'startDate': start_date, 'endDate': end_date}
    index = requests.get(api, params).json().get('data')
    drop_col = ['indexNameCnAll', 'indexNameCn', 'indexNameEnAll', 'indexNameEn']
    df = pd.DataFrame(index).drop(columns=drop_col, errors='ignore')
    df.to_csv(path_or_buf=f"中证指数/{name}-{code}.csv", mode=mode, index=False, header=header)

# 搜索指数
def search(search_input):
    api = "https://www.csindex.com.cn/csindex-home/index-list/query-index-item"
    data = {"sorter": {"sortField": None, "sortOrder": None}, "pager": {"pageNum": 1, "pageSize": 10},
            "searchInput": search_input,
            "indexFilter": {"ifCustomized": None, "ifTracked": None, "ifWeightCapped": None, "indexCompliance": None,
                            "hotSpot": None, "indexClassify": None, "currency": None, "region": None,
                            "indexSeries": None, "undefined": None}
            }
    index = requests.post(api, json=data).json().get('data') or []
    return [{'indexCode': i['indexCode'], 'indexName': i['indexName'], 'publishDate': i['publishDate']} for i in index]
    # print(index['indexCode'],index['indexName'],index['publishDate'],index['assetsClassify'],index['consNumber'])


