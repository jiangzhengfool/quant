# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:14:13 2021

@author: w
"""
import pandas as pd
import numpy as np
from DualThrust import Dual_Thrust

# 读取训练数据集
# train_data = pd.read_csv('文件1.样本训练数据.csv',encoding='gbk')
# val_data = pd.read_csv('文件2.回测数据.csv',encoding='gbk')

full_data = pd.read_csv('DataSet/RB9.csv', index_col=0, header=None,
                        names=[ '开盘价', '最高价', '最低价', '收盘价', '成交量'])



params_testing_2018_hourly = {}
params_testing_2019_hourly = {}
params_testing_2020_hourly = {}
params_testing_2021_hourly = {}
params_testing = [params_testing_2021_hourly]

n_list = [5,10,15,20,25]


k1_list = [0.1,0.3,0.5,0.7,1.0]
k2_list = [0.1,0.3,0.5,0.7,1.0]

# 14 0.3 0.1

# [19, 0.5, 0.5]  0.740806

# [20, 0.5, 0.1]
# 0.98273
for n in n_list:
    for i in k1_list:
        for j in k2_list:
            dual = Dual_Thrust(N=n, K1=i, K2=j, Freq='D')
            dual.Input(Data =full_data, Cap = 10000, Tran_fee = 0.003)
            dual.trading()
            #dual.evaluate_stats()
            params_testing[0][str([n,i,j])] = dual.Return()
            print(str([n,i,j]),'One test finished')

df_params_testing_2021 = pd.DataFrame(list(params_testing_2021_hourly.items()),columns = ['param_settings','return'])
df_params_testing_2021.to_csv('result.csv')
max_return = df_params_testing_2021[df_params_testing_2021['return']==df_params_testing_2021['return'].max()]
print(max_return)

"""
dual = Dual_Thrust(N=20, K1=0.01, K2=0.03, Freq='D')
dual.Input(Data=full_data, Cap=10000, Tran_fee=0.003)
dual.trading()
dual.evaluate_stats()
dual.show_return()
sample = dual.return_data()

"""




# sample.tail()
#
# start = 333
# end = 364
# print(sample[start:end]['Short_signal'] * sample[start:end]['Trading_action'])
# print('Transaction No. is: %s ' % (sum(sample[start:end]['Short_signal'] * sample[start:end]['Trading_action'])))
#
# dual.MaxDrawdown(sample['BenchMark'])
#
# sharp_mean = np.mean(sample['BenchMark'])
# sharp_std = np.std(sample['BenchMark'])  # Standard Deviation of returns
# Sharp_Ratio = (sharp_mean - 0.04) / sharp_std
# print(Sharp_Ratio)

# Get maximum value from a dictionary
# 1Day

#
# print(max(params_testing_2018_hourly, key=params_testing_2018_hourly.get))
# print(params_testing_2018_hourly[max(params_testing_2018_hourly, key=params_testing_2018_hourly.get)])
# print(max(params_testing_2020_hourly, key=params_testing_2020_hourly.get))
# print(params_testing_2020_hourly[max(params_testing_2020_hourly, key=params_testing_2020_hourly.get)])
#

# 1Day
# 2018: [2, 2.0, 1.5] = 0.34983909634674565
# 2019: [2, 0.5, 1.5] = 2.501846072095831
# 4hour
# 2018: [4, 2.5, 1.5] = 0.5730103232646645
# 2020: [3, 3.0, 1.5] = 3.0603314583624837
