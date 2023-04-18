import os
import pandas as pd
import requests
from datetime import timedelta, datetime
from sqlalchemy import NVARCHAR, text

from sql.database import engine


# 获取中证指数截至前一天每日数据
def get_day(code, name, start_date='19900101', end_date=(datetime.today() + timedelta(-1)).strftime('%Y%m%d')):
    filename = f"中证指数/{name}-{code}.csv"
    mode = 'w'
    header = True
    is_save = True
    if os.path.exists(filename) and os.path.getsize(filename):
        mode = 'a'
        header = False
        last_date = f"{pd.read_csv(filename).tail(1)['tradeDate'].reset_index(drop=True)[0]}"
        if last_date == end_date: is_save = False
        start_date = (datetime.strptime(last_date, "%Y%m%d") + timedelta(1)).strftime('%Y%m%d')
    if is_save:
        api = "https://www.csindex.com.cn/csindex-home/perf/index-perf"
        params = {'indexCode': code, 'startDate': start_date, 'endDate': end_date}
        index = requests.get(api, params).json().get('data')
        print(index)
        drop_col = ['indexCode', 'indexNameCnAll', 'indexNameCn', 'indexNameEnAll', 'indexNameEn']
        df = pd.DataFrame(index).drop(columns=drop_col, errors='ignore').rename(columns={'tradeDate':'time'})
        df.dropna(how='any', subset=['open', 'high', 'low', 'close'], inplace=True)  # 过滤掉某些列值为空的行
        df.drop_duplicates(subset=['time'], inplace=True)  # 过滤掉重复行
        df.to_csv(path_or_buf=f"中证指数/{name}-{code}.csv", mode=mode, index=False, header=header)
    data = pd.read_csv(filepath_or_buffer=f"中证指数/{name}-{code}.csv", parse_dates=['time'],
                       date_parser=lambda x: datetime.strptime(x, "%Y%m%d"))
    print(data)


# save_day('931151', '光伏产业')


# 存储中证指数
def save():
    api = "https://www.csindex.com.cn/csindex-home/index-list/query-index-item"
    data = {"sorter": {"sortField": None, "sortOrder": None}, "pager": {"pageNum": 1, "pageSize": 9999},
            # "searchInput": search_input,
            "indexFilter": {"ifCustomized": None, "ifTracked": None, "ifWeightCapped": None, "indexCompliance": None,
                            "hotSpot": None, "indexClassify": None, "currency": None, "region": None,
                            "indexSeries": None, "undefined": None}
            }
    index = requests.post(api, json=data).json().get('data')
    if index:
        df = pd.DataFrame(index)

        df.to_sql('zhongzheng_index', con=engine, if_exists='replace', index=False,
                  dtype={'indexCode': NVARCHAR(length=255), })
        with engine.connect() as con:
            con.execute(text("alter table zhongzheng_index add primary key (indexCode);"))
    else:
        print('数据为空')
    # return index
    # return [{'indexCode': i['indexCode'], 'indexName': i['indexName']} for i in index]
    # print(index['indexCode'],index['indexName'],index['publishDate'],index['assetsClassify'],index['consNumber'])

# 模糊搜索指数
def search(input):
    print(input)
    with engine.begin() as conn:
        sql = text(f"select * from zhongzheng_index where concat(indexName, indexCode) like '%{input}%';")
        return conn.execute(sql).mappings().all()
