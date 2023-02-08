# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 17:35:15 2022

@author: kutay
"""


import pandas as pd
my_series=pd.Series([10,20,30,40])
print(my_series.ndim) #1

#The “head()” function returns a specified number of elements at the beginning of a series. 
print(my_series.head(2))
""" 0    10
    1    20
   dtype: int64"    #ilk 2 sini bastırdı
"""
print(my_series.tail(2))
""" 
2    30
3    40
dtype: int64 #sson 2sini aldı


"""

print(my_series[2]) #30

numbers=[[1,2,3,4,5,6],[1,2,3,4,5,6]]
dataframe=pd.DataFrame(numbers) 
print(dataframe.describe())