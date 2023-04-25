import pandas as pd
import time

import numpy as np
import polars as pl
import talib as tb
import requests
import os
from datetime import timedelta, datetime
from sqlalchemy import NVARCHAR, text

from app.indicator import td913
from helper.my_http import crawler
from sql.database import engine


# 获取指数截至前一天每日数据
def get_day(name, code, source, start_date='1990-01-01', end_date=datetime.today().strftime('%Y-%m-%d'), path="./"):
    s = time.perf_counter()
    print(s)
    filename = f"{path}data/{name}-{code}.csv"
    print(filename)
    mode = 'wb'
    header = True
    is_save = True
    if os.path.exists(filename) and os.path.getsize(filename):
        mode = 'ab'
        header = False
        last_date = f"{pl.read_csv(filename).tail(1)['time'][0]}"
        print(last_date)
        if last_date == end_date: is_save = False
        start_date = (datetime.strptime(last_date, "%Y-%m-%d") + timedelta(1)).strftime('%Y-%m-%d')
    for x in range(1):
        if is_save:
            if source == 'Z':
                ZHONGZHENG_API = "https://www.csindex.com.cn/csindex-home/perf/index-perf"
                ZHONGZHENG_PARAMS = {'indexCode': code, 'startDate': start_date.replace('-', ''),
                                     'endDate': end_date.replace('-', '')}
                z_index = crawler(ZHONGZHENG_API, ZHONGZHENG_PARAMS)
                if not z_index: break
                df = pl.from_dicts(z_index, infer_schema_length=None).select(
                    ['tradeDate', 'open', 'close', 'high', 'low', 'change', 'changePct', 'tradingVol'])
                df = df.with_columns(
                    pl.col('tradeDate').apply(lambda t: datetime.strptime(t, "%Y%m%d").strftime('%Y-%m-%d')))
            elif source == 'G':
                GUOZHENG_API = "http://hq.cnindex.com.cn/market/market/getIndexDailyData"
                GUOZHENG_PARAMS = {'indexCode': code, 'startDate': start_date, 'endDate': end_date}
                g_index = crawler(GUOZHENG_API, GUOZHENG_PARAMS).get('data')
                if not g_index: break
                # timestamp,current,high,open,low,close,chg,percent,amount,volume,avg
                # ['timestamp', 'current', 'high', 'open', 'low', 'close', 'chg', 'percent', 'amount', 'volume', 'avg']
                df = pl.from_records(g_index, orient='row',
                                     schema=['timestamp', 'current', 'high', 'open', 'low', 'close', 'chg', 'percent',
                                             'amount', 'volume', 'avg']).select(
                    ['timestamp', 'open', 'close', 'high', 'low', 'chg', 'percent', 'volume']).with_columns(
                    pl.col('timestamp').apply(lambda t: datetime.fromtimestamp(t / 1000).strftime('%Y-%m-%d')),
                    pl.col('percent') * 100, pl.col('volume') / 1000)
            df.columns = ['time', 'open', 'close', 'high', 'low', 'chg', 'chgp', 'vol']
            # 预处理
            df = df.drop_nulls(['open', 'high', 'low', 'close'])
            # print(df[:100])
            df = df.unique(maintain_order=True)  # 过滤掉重复行
            if df.is_empty(): break
            # BOLL
            df = df.with_columns(pl.DataFrame(tb.BBANDS(df['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0),
                                              schema=['bollUpper', 'bollMiddle', 'bollLower']))
            # KDJ
            df = df.with_columns(
                pl.DataFrame(tb.STOCH(df['high'], df['low'], df['close'], fastk_period=9, slowk_period=5,
                                      slowk_matype=1, slowd_period=5, slowd_matype=1), schema=['slowK', 'slowD']), )
            df = df.with_columns(slowJ=3 * pl.col('slowK') - 2 * pl.col('slowD'))
            # print(df[:100])
            # 九转序列
            df = td913(df)
            # ENE 轨道线
            N, M1, M2 = 10, 11, 9
            df = df.with_columns(eneUpper=(1 + M1 / 100) * tb.MA(df['close'], N),
                                 eneLower=(1 - M1 / 100) * tb.MA(df['close'], N))

            df = df.fill_nan(0).fill_null(0)
            with open(filename, mode=mode) as f:
                df.write_csv(f, has_header=header, float_precision=2)
                f.close()
    data = pl.read_csv(filename)
    e = time.perf_counter()
    print(s - e)
    return data.to_dicts()
    # try:
    #
    # finally:


# get_day('创业板指', '399006', 'G', path='../')


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
    pd.concat([z_df, g_df]).to_sql('stock_index', con=engine, if_exists='replace', index=False,
                                   dtype={'code': NVARCHAR(length=255), })
    with engine.connect() as con:
        con.execute(text("alter table stock_index add primary key (code);"))


# 模糊搜索指数
def search(input_value):
    with engine.begin() as conn:
        sql = text(
            f"select * from stock_index where concat(name, code) like '%{input_value}%';")
        return conn.execute(sql).mappings().all()
