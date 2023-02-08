# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 14:18:38 2022

@author: kutay
"""
#DATA PROCESSING 
names= ['Ben', 'Omer', 'Karen', 'Celine', 'Sue', 'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude']
Number_of_calls= [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
Average_deal_size= [8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
Revenues= [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]

import numpy as np
#We need to prepare an array in which we will store the values.
data=np.array([],dtype=int) #dtype içine hangi tipte veri gönderebileceğimizi blirlememizi sağlar.
#Since we have integer data, we use dtype=int. 
#Note that dtype defaults to float, therefore all the values that are added to the array will be converted to float. 
# we don’t want to use string type values in NumPy data structures. 
#So instead of adding names directly, we will add the index of each name.
def append_names(names_list):
    global data
    for i in names_list:
        data=np.append(data,names.index(i))
        
def append_performance_measure(feature_list):
    # We give the lists one by one as arguments, 
    #and inside the function we’ll directly add them to the NumPy array, since they only have numerical data. 
    global data
    data=np.append(data,feature_list) 
    
#Now we can call the functions to add the data to our array. 
#Let’s print the “data” array and its shape to see what we have. 

append_names(names)
append_performance_measure(Number_of_calls)
append_performance_measure(Average_deal_size)
append_performance_measure(Revenues)

print(data) #shape= (44, )#1d
data=data.reshape(4,11) #1.column nofcalls 2.column ads 3.column revenue
print(data) #2d
print(data[0])
print(data[1])
print(data[2])  #each row is index
print(data[3])

#revenue by ellen
print(data[3][7]) #or  print(data[3,7])  #3.row x 7.column 

def calculate_performance(employee_name):
    idx=names.index(employee_name)
    numberofcalls=data[1,idx]
    averagedealsize=data[2,idx]
    revenue=data[3,idx]
    
    score= (averagedealsize * revenue)/numberofcalls
    
    return score

print(calculate_performance("Ellen"))

#calculate performance of each employee

performance_score=list()

for i in names:
    scores=calculate_performance(i)
    scores=int(scores)
    performance_score.append(scores)
    
#add the scores to data array
#Using Numpy’s .concatenate() method, we can add the “performance_scores” list to our “data” array. 
#The first argument is our “data” array, followed by our performance_scores list.  
    
data=np.concatenate((data,[performance_score]),axis=0) #0 represent y axis #5.satıra performanslar eklendi.
#◙Notice that we pass the “performance_scores” list inside squared brackets. 
#Because our “data array” is 2 dimensional we have to give our performance list as a 2D-array as well.
#here is also another argument called “axis” which we set to 0. 
#This argument is used to specify along which axis the new data will be added. The value 0 indicates the vertical axis, while the value 1 indicates the horizontal axis. 
print(data)   

#find out best and worst perfomance score

idx_best_employee=np.argmax(data[4]) #5.satırdaki en yüksek indeksi döner
idx_worst_employee=np.argmin(data[4]) #5.satırdaki en düşük indeksi döner
    
print(f"Best Performance:{names[idx_best_employee]}") 
print(f"Worst Performance:{names[idx_worst_employee]}")       
        
