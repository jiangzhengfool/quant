# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from DualThrust import Dual_Thrust


full_data = pd.read_csv('RB9.csv', index_col=0, header=None,
                        names=[ '开盘价', '最高价', '最低价', '收盘价', '成交量'])





dual = Dual_Thrust(N=20, K1=0.5, K2=0.5, Freq='D')
dual.Input(Data=full_data, Cap=10000, Tran_fee=0.003)
dual.trading()
dual.evaluate_stats()
dual.show_return()
sample = dual.return_data()




