import numpy as np
import pandas as pd
import talib as tb
import requests
import os
from datetime import timedelta, datetime
from sqlalchemy import NVARCHAR, text
from sql.database import engine


# 获取指数截至前一天每日数据
def get_day(name, code, source, start_date='1990-01-01', end_date=datetime.today().strftime('%Y-%m-%d')):
    filename = f"data/{name}-{code}.csv"
    mode = 'w'
    header = True
    is_save = True
    # pd.set_option('display.max_rows', None)
    try:
        if os.path.exists(filename) and os.path.getsize(filename):
            mode = 'a'
            header = False
            last_date = f"{pd.read_csv(filename).tail(1)['time'].reset_index(drop=True)[0]}"
            if last_date == end_date: is_save = False
            start_date = (datetime.strptime(last_date, "%Y-%m-%d") + timedelta(1)).strftime('%Y-%m-%d')
        # print(start_date, end_date)
        if is_save:
            if source == 'Z':
                ZHONGZHENG_API = "https://www.csindex.com.cn/csindex-home/perf/index-perf"
                ZHONGZHENG_PARAMS = {'indexCode': code, 'startDate': start_date.replace('-', ''),
                                     'endDate': end_date.replace('-', '')}
                z_index = requests.get(ZHONGZHENG_API, ZHONGZHENG_PARAMS).json().get('data')
                df = pd.DataFrame(z_index)[['tradeDate', 'open', 'close', 'high', 'low', 'tradingVol']]
                df['tradeDate'].apply(lambda t: datetime.strptime(t, "%Y%m%d").strftime('%Y-%m-%d'))
            elif source == 'G':
                GUOZHENG_API = "http://hq.cnindex.com.cn/market/market/getIndexDailyData"
                GUOZHENG_PARAMS = {'indexCode': code, 'startDate': start_date, 'endDate': end_date}
                g_index = requests.get(GUOZHENG_API, GUOZHENG_PARAMS).json().get('data').get('data')
                # timestamp,current,high,open,low,close,chg,percent,amount,volume,avg
                df = pd.DataFrame(g_index)[[0, 3, 5, 2, 4, 9]]
                df[0] = df[0].apply(lambda t: datetime.fromtimestamp(t / 1000).strftime('%Y-%m-%d'))
            df.columns = ['time', 'open', 'close', 'high', 'low', 'vol']
            # 预处理
            df.dropna(how='any', subset=['open', 'high', 'low', 'close'], inplace=True)  # 过滤掉某些列值为空的行
            df.drop_duplicates(subset=['time'], inplace=True)  # 过滤掉重复行
            df.reset_index(drop=True, inplace=True)  # 重排索引
            # BOLL
            df['bollUpper'], df['bollMiddle'], df['bollLower'] = \
                tb.BBANDS(df['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
            # KDJ
            df['slowK'], df['slowD'] = tb.STOCH(df['high'], df['low'], df['close'], fastk_period=9, slowk_period=5,
                                                slowk_matype=1, slowd_period=5, slowd_matype=1)
            df['slowJ'] = list(map(lambda x, y: 3 * x - 2 * y, df['slowK'], df['slowD']))
            # df['dif'], df['dea'], df['macd'] = tb.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)

            # 九转序列
            df['td9'] = 2
            for i in range(1, len(df['close']) - 4 + 1):
                for k in range(9):
                    if i + k + 4 < len(df['close']):
                        if df['close'][i + k] < df['close'][i + k + 4]:
                            if k == 8:
                                # print(df['time'][i + k + 4])
                                df.loc[i + k + 4, 'td9'] = 0
                            continue
                        else:
                            break
                for k in range(9):
                    if i + k + 4 < len(df['close']):
                        if df['close'][i + k] > df['close'][i + k + 4]:
                            if k == 8:
                                # print(df['time'][i + k + 4])
                                df.loc[i + k + 4, 'td9'] = 1
                            continue
                        else:
                            break
            # ENE 轨道线
            N, M1, M2 = 10, 11, 9
            df['eneUpper'] = (1 + M1 / 100) * tb.MA(df['close'], N)
            df['eneLower'] = (1 - M1 / 100) * tb.MA(df['close'], N)
            df.fillna(0, inplace=True)  # 填充剩下的空值
            df.round({'bollUpper': 2, 'bollMiddle': 2, 'bollLower': 2, 'slowK': 2, 'slowD': 2, 'slowJ': 2, 'eneUpper': 2,
                      'eneLower': 2}).to_csv(
                path_or_buf=filename, mode=mode, index=False,
                header=header)
    finally:
        data = pd.read_csv(filepath_or_buffer=filename)
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
