import numpy as np
import pandas as pd
import talib
from talib import BBANDS


# all_ta_label = talib.get_functions()
# print(len(all_ta_label))
#
# all_ta_groups = talib.get_function_groups()
#
# print(all_ta_groups)


# 布林带
def boll(olhc):
    up, middle, low = BBANDS(olhc['close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    # ch = (up - low) / middle
    # delta = np.r_[np.nan, np.diff(ch)]
    data = dict(upper=up, middle=middle, lower=low)
    df = pd.DataFrame(data, index=df.index, columns=['upper', 'middle', 'lower']).dropna()
    print(up, middle, low, ch, delta)

