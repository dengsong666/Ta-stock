import time

import numpy as np
import pandas as pd
import talib as tb
import requests
from datetime import datetime
from sqlalchemy import text, VARCHAR

from helper.my_http import crawler
from sql.database import get_engine

up = down = 0


# 获取指数截至前一天每日数据
def get_day(name, code, source, start_date='1990-01-01', end_date=datetime.today().strftime('%Y-%m-%d')):
    s = time.perf_counter()
    table_name = f"{name}_{code}"
    print(table_name)
    for x in range(1):
        if source == 'Z':
            ZHONGZHENG_API = "https://www.csindex.com.cn/csindex-home/perf/index-perf"
            ZHONGZHENG_PARAMS = {'indexCode': code, 'startDate': start_date.replace('-', ''),
                                 'endDate': end_date.replace('-', '')}
            # print(requests.get(ZHONGZHENG_API, ZHONGZHENG_PARAMS).text)
            z_index = crawler(ZHONGZHENG_API, ZHONGZHENG_PARAMS)
            if not z_index: break
            df = pd.DataFrame(z_index)[
                ['tradeDate', 'open', 'close', 'high', 'low', 'change', 'changePct', 'tradingVol']]
            df['tradeDate'] = df['tradeDate'].apply(lambda t: datetime.strptime(t, "%Y%m%d").strftime('%Y-%m-%d'))
        elif source == 'G':
            GUOZHENG_API = "http://hq.cnindex.com.cn/market/market/getIndexDailyData"
            GUOZHENG_PARAMS = {'indexCode': code, 'startDate': start_date, 'endDate': end_date}
            g_index = crawler(GUOZHENG_API, GUOZHENG_PARAMS).get('data')
            if not g_index: break
            # timestamp,current,high,open,low,close,chg,percent,amount,volume,avg
            df = pd.DataFrame(g_index)[[0, 3, 5, 2, 4, 6, 7, 9]]
            df[7] = (df[7] * 100).round(2)
            df[9] = (df[9] / 1000000).round(2)
            df[0] = df[0].apply(lambda t: datetime.fromtimestamp(t / 1000).strftime('%Y-%m-%d'))
        df.columns = ['time', 'open', 'close', 'high', 'low', 'chg', 'chgp', 'vol']
        # 预处理
        df.dropna(how='any', subset=['open', 'high', 'low', 'close'], inplace=True)  # 过滤掉某些列值为空的行
        df.drop_duplicates(subset=['time'], inplace=True)  # 过滤掉重复行
        df.reset_index(drop=True, inplace=True)  # 重排索引
        if df.empty: break
        # BOLL
        df['bollUpper'], df['bollMiddle'], df['bollLower'] = \
            tb.BBANDS(df['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
        # KDJ
        df['slowK'], df['slowD'] = tb.STOCH(df['high'], df['low'], df['close'], fastk_period=9, slowk_period=5,
                                            slowk_matype=1, slowd_period=5, slowd_matype=1)
        df['slowJ'] = list(map(lambda x, y: 3 * x - 2 * y, df['slowK'], df['slowD']))

        # df['dif'], df['dea'], df['macd'] = tb.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)

        # 九转序列
        def inner(diff):
            global up, down
            if diff > 0:
                if up == 13: up = 0
                up, down = up + 1, 0
                return up
            else:
                if down == -13: down = 0
                up, down = 0, down - 1
                return down

        df['td913'] = df['close'].diff(periods=4).apply(lambda d: inner(d))
        # ENE 轨道线
        N, M1, M2 = 10, 11, 9
        df['eneUpper'] = (1 + M1 / 100) * tb.MA(df['close'], N)
        df['eneLower'] = (1 - M1 / 100) * tb.MA(df['close'], N)
        df.fillna(0, inplace=True)  # 填充剩下的空值
        # print(df.round(2))
        df.round(2).to_sql(table_name, con=get_engine(), if_exists='replace', index=False, dtype={'time': VARCHAR(50)})
    data = pd.read_sql(table_name, con=get_engine())
    return data.to_dict('records')


# 存储指数
def save():
    ZHONGZHENG_API = "https://www.csindex.com.cn/csindex-home/index-list/query-index-item"
    GUOZHENG_API = "http://www.cnindex.com.cn/index/indexList"
    ZHONGZHENG_PARAMS = {"sorter": {"sortField": None, "sortOrder": None}, "pager": {"pageNum": 1, "pageSize": 9999},
                         "indexFilter": {"ifCustomized": None, "ifTracked": None, "ifWeightCapped": None,
                                         "indexCompliance": None,
                                         "hotSpot": None, "indexClassify": None, "currency": None, "region": None,
                                         "indexSeries": None, "undefined": None}
                         }

    GUOZHENG_PARAMS = {"channelCode": -1, "pageNum": 1, "rows": 9999, }
    # indexCode indexName consNumber indexSeries indexClassify:规模|行业|风格|主题|策略|综合|债券|基金
    zhongzheng_index = requests.post(ZHONGZHENG_API, json=ZHONGZHENG_PARAMS).json().get('data')
    z_df = pd.DataFrame(zhongzheng_index)[['indexCode', 'indexName', 'indexSeries', 'indexClassify', 'consNumber']]
    z_df.columns = ['code', 'name', 'series', 'classify', 'size']
    z_df.dropna(how='any', subset=['size'], inplace=True)  # 过滤掉某些列值为空的行

    z_df['series'] = z_df['series'].str.replace('系列指数', '').replace('指数系列', '')
    z_df['size'] = z_df['size'].astype(str).astype(np.int64)
    z_df['source'] = 'Z'
    # indexcode indexname samplesize indextype：1.深圳 2.国证 3.央视 5.中华 7.全球
    guozheng_index = requests.get(GUOZHENG_API, params=GUOZHENG_PARAMS).json().get('data').get('rows')

    g_df = pd.DataFrame(guozheng_index)[['indexcode', 'indexname', 'indextype', 'samplesize']]
    g_df.columns = ['code', 'name', 'type', 'size']
    g_df.dropna(how='any', subset=['size'], inplace=True)  # 过滤掉某些列值为空的行
    g_df['series'], g_df['classify'] = g_df['type'].str[:1], g_df['type'].str[-2:]

    g_df['series'].replace(['1', '2', '3', '5', '7'], ['深证', '国证', '央视', '中华', '全球'], inplace=True)
    g_df['classify'].replace(['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '11'],
                             ['规模', '行业', '风格', '主题', '策略', '综合', '债券', '基金', '定制', '人民币', '其他'],
                             inplace=True)
    g_df.drop(columns=['type'], inplace=True)
    g_df['source'] = 'G'
    print(z_df[:10], g_df[:10])
    pd.concat([z_df, g_df]).to_sql('stock_index', con=get_engine('../'), if_exists='replace', index=False)


# save()
# 模糊搜索指数
def search(input_value):
    with get_engine().begin() as conn:
        sql = text(f"select * from stock_index where name like '%{input_value}%' or code like '%{input_value}%';")
        return conn.execute(sql).mappings().all()
