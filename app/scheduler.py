import functools
import os

import pandas as pd
import yagmail

from schedule import every, repeat, run_pending, CancelJob
import time

from sqlalchemy import text

from app.index import get_day
from sql.database import engine


def catch_exceptions(cancel_on_failure=False):
    def catch_exceptions_decorator(job_func):
        @functools.wraps(job_func)
        def wrapper(*args, **kwargs):
            try:
                return job_func(*args, **kwargs)
            except:
                import traceback
                print(traceback.format_exc())
                if cancel_on_failure:
                    return CancelJob

        return wrapper

    return catch_exceptions_decorator


# @catch_exceptions(cancel_on_failure=True)
# @repeat(every(1).seconds)
def send_email():
    # 发送邮件
    print(111)
    # 链接邮箱服务器
    yag = yagmail.SMTP(user="ds-137@qq.com", password="hywdcgazqaiagghj", host='smtp.qq.com')

    yag.send(to='1487907946@qq.com', subject='哈哈哈', contents='小宝贝')
    yag.close()


# @catch_exceptions(cancel_on_failure=True)
# @repeat(every(1).seconds)
def update_index():
    with engine.begin() as conn:
        sql = text(f"select * from stock_index")
        df = pd.DataFrame(conn.execute(sql).fetchall())
        df.apply(lambda x: get_day(x['name'], x['code'], x['source'], path="../"), axis=1)


update_index()
# get_day('科创50', '000688', 'Z', path="../")     0
while True:
    run_pending()
    time.sleep(1)
