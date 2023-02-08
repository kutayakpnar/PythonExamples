# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:40:33 2022

@author: kutay
"""


#GUIDED PROJECT DATA PROCESSING WITH NUMPY



names=["Ben", "Omer", "Karen", "Celine", "Sue","Bora","Rose", "Ellen", "Bob", "Taylor", "Jude"]
Number_of_calls=[300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
Average_deal_size=[8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
Revenues=[2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]


import numpy as np 
data=np.array([], dtype=int) #While creating arrays,
# we can define what kind of data we will have in the array with the dtype parameter. 
def append_names(names_list):
    global data
    for i in names_list:
        data=np.append(data,names.index(i))

def append_performance(feature_list):
    global data
    data=np.append(data,feature_list)

append_names(names)

append_performance(Number_of_calls)
append_performance(Average_deal_size)
append_performance(Revenues)
data=data.reshape(4,11)
print(data)


print(data.shape)

print(data[0]) #['0' '1' '2' '3' '4' '5' '6' '7' '8' '9' '10']
print(data[1])
print(data[2])

print(data[3,7]) #6000 ellens revenue

def calculate_performance(employeename):
    idx=names.index(employeename)
    numberofcalls=data[1,idx]
    averagedealsize=data[2,idx]
    revenue=data[3,idx]
    
    score=int(averagedealsize)*int(revenue)/int(numberofcalls)
    return score

print(calculate_performance("Ellen"))

performance_scores=[]
for name in names:
    score=int(calculate_performance(name))
    performance_scores.append(score)
print([performance_scores])
data=np.concatenate((data,[ performance_scores ] ), axis=0)


idx_best=np.argmax(data[4])

idx_worst=np.argmin(data[4])



print(f"Best:{names[idx_best]}")
print(f"Worst:{names[idx_worst]}")

    

