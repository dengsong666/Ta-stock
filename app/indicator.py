import polars as pl

up = down = 0
# 九转序列
def td9(df):

    def inner(diff):
        global up, down
        if diff > 0:
            if up == 9: up = 0
            up, down = up + 1, 0
            return up
        else:
            if down == -9: down = 0
            up, down = 0, down - 1
            return down

    return df.with_columns(td9=pl.col('close').diff(n=4).apply(lambda d: inner(d)))
