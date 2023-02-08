# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:14:04 2022

@author: kutay
"""


#DATA MANIPULATION WITH PANDAS

import pandas as pd
import numpy as np 

last_year=pd.read_csv("employee_revenue_lastyear.csv")
print(last_year.head()) #prints the first 5 rows
print(last_year.tail()) 
#prints the last 5 rows

print(last_year.shape) #(11, 4)
print(last_year.info())
last_year["Year:"]=2021

names= np.array(["Ben", "Omer", "Karen", "Celine", "Sue", "Bora", "Rose", "Ellen", "Bob", "Taylor", "Jude"])
Number_of_calls =np.array( [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80])
Average_deal_size = np.array([8,6,24,32, 5,25,25,40, 15, 10, 12])
Revenues =np.array( [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500])

dictionary={"name":names,
            "calls":Number_of_calls,
            "avgdealsize":Average_deal_size,
            "revenue":Revenues}
current_year=pd.DataFrame(dictionary)
print(current_year.head())
current_year["Year:"]=2022
print(current_year.head())

#But you might have noticed a problem: the column names of the DataFrame are different from last year’s DataFrame. 
#This will cause an error if we try to merge the two DataFrames. Let’s fix this
#Let’s fix this. We assign the column names of the last_year DataFrame to the current_year DataFrame using the columns attribute. 
current_year.columns=last_year.columns #they have the same names for each column

all_data=pd.concat([last_year , current_year] , axis=0)
print(all_data) # when print notice that indexes are incorrect

#The solution is simple; we use the reset_index() function which creates new index numbers. 
#We set the argument inplace equals True, so the function updates the DataFrame itself.
#Also, we have to set the drop argument to True so that old indexes are deleted; 
#otherwise a new column with the old index values will be created.
all_data.reset_index(drop=True,inplace=True)
"""ut we also need to have a look at the data entries. 
We start with checking if there are any missing values. 
To do this, we use a method called .isna(). 
This returns an output of boolean, so-called True and False values for each element in a DataFrame that indicates whether an element is not available. 
And by adding .any() we get a short table telling us if we have any True value -missing value in our case- in a given column.
 We can see that there are missing values in “Average deal size” and “Revenue” columns. """

print(all_data.isna().any())

#When we run fillna() all the missing values will be replaced with the value that we put in for the argument.
# Here, we want to fill the missing values with the mean of the respective column. 
#To do so, we set the argument to “np.mean(all_data)”
all_data.fillna(value=np.mean(all_data),inplace=True)
#lso, there might be some duplicated rows, 
#let’s drop them by using the .drop_duplicates() method and print the DataFrame again.

all_data.drop_duplicates(inplace=True)
all_data.reset_index(drop=True)
print(all_data.describe())
"""print(all_data[all_data["Year:"]==2021].decribe())
print(all_data[all_data["Year:"]==2022].decribe())"""
print(all_data.sort_values(by="Revenue"))
print(all_data["Name"].value_counts())






















