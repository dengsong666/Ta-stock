import numpy as np
import pandas as pd
import talib as tb
from talib import BBANDS


# all_ta_label = talib.get_functions()
# print(len(all_ta_label))
#
# all_ta_groups = talib.get_function_groups()
#
# print(all_ta_groups)


# 轨道线
def ene(close,N=25,M1=6,M2=6):

    UPPER =  (1 + M1 / 100) * tb.MA(close,N)
    LOWER = (1 - M2 / 100) * tb.MA(close, N);

