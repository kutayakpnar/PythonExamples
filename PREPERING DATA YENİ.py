# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 12:56:38 2022

@author: kutay
"""

"""
with open("employee_revenue.txt","r",encoding="utf-8") as file:
    data=file.read()
    lines=data.splitlines() #\n olan yerden itibaren böler.Her bir cümle listenin bir elemanı olur.
    string=lines[0]
    #print(string)        farkettik ki başta ve sonda gereksiz boşluklar var bunu düzenlememiz lazım.
    string=string.strip(" ")
    print(string)
    #genel metine baktığımızda harflerin büyük ve küçük yazımıyla alakalı hatalar var bunları düzeltelim.
    string=string.lower() #tüm harfler küçük oldu.
    #şimdi cümlenin başını yani isimi büyük harfle başlatalım.
    string=string.capitalize()
    print(string)
    #We got a clear string, now we can proceed to extract information. For this, we need to split the sentence into words.
    #We use the split() method to split the string and store each word as an element in a list. Let’s take a look. 
    split_string=string.split()
    #We see that the first element of the list contains a name
    name=split_string[0]
    #Next, we see that the element with the index 2 contains the number of calls made by each employee.
    call_number=split_string[2]
    #The sentence structure is not the same for all strings after the 7th word, 
    #so we’ll use a different technique to get the average deal size. 
    #kily, all deal size amounts have the dollar sign next to them. 
    #So we can use the $ symbol to identify the element corresponding to the deal size.  
    for i in split_string:
        if "$" in i:
            average_deal_size=i.split("$")[0]
            
    #To extract the revenue, we can use a similar method. 
    #We can use the string “dollars” to extract the revenue, which is the element right before “dollars”.
    dollars_index=split_string.index("dollars")
    revenue_index=dollars_index-1
    revenue=split_string[revenue_index]
    #we extracted all necessary information.
    
print("Name:",name)
print("Number of Calls:",call_number)
print("Average Deal Size:",average_deal_size)
print("Revenue:",revenue)
#Notice that all the variables are string  beacue they were extracted from our text file.
#But they should be integers.
call_number=int(call_number)
averaga_deal_size=int(average_deal_size)
revenue=int(revenue)

#but we got these for the first employee.
#lets do it for every employee"""
"""
names=[]
call_numbers=[]
average_deal_sizes=[]
revenues=[]
with open("employee_revenue.txt","r",encoding="utf-8") as file:
    data=file.read()
    lines=data.splitlines()
    for employee in lines:
        employee=employee.strip()
        employee=employee.lower()
        employee=employee.capitalize()
        
        split_employee=employee.split()
        name=split_employee[0]
        call_number=split_employee[2]
        
        for i in split_employee:
            if "$" in i:
                average_deal_size=i
                
        average_deal_size=average_deal_size.split("$")[0]
        
        dollars_index=split_employee.index("dollars")
        revenue_index=dollars_index-1
        revenue=split_employee[revenue_index]
        
        call_number=int(call_number)
        average_deal_size=int(average_deal_size)
        revenue=int(revenue)
        
        names.append(name)
        call_numbers.append(call_number)
        average_deal_sizes.append(average_deal_size)
        revenues.append(revenue)
        
print("Name:",names)
print("Number of Calls:",call_numbers)
print("Average Deal Size:",average_deal_sizes)
print("Revenue:",revenues)       """ 
    
#We can transform these codes into funtion.    
    

with open("employee_revenue.txt","r",encoding="utf-8") as file:
    data=file.read()
    lines=data.splitlines()
    def cleanlines(lines):
        names=[]
        call_numbers=[]
        average_deal_sizes=[]
        revenues=[]
        
        for employee in lines:
            employee=employee.strip()
            employee=employee.lower()
            employee=employee.capitalize()
        
            split_employee=employee.split()
            name=split_employee[0]
            call_number=split_employee[2]
        
            for i in split_employee:
                if "$" in i:
                    average_deal_size=i
                
            average_deal_size=average_deal_size.split("$")[0]
        
            dollars_index=split_employee.index("dollars")
            revenue_index=dollars_index-1
            revenue=split_employee[revenue_index]
        
            call_number=int(call_number)
            average_deal_size=int(average_deal_size)
            revenue=int(revenue)
        
            names.append(name)
            call_numbers.append(call_number)
            average_deal_sizes.append(average_deal_size)
            revenues.append(revenue)    
    
        return names,call_numbers,average_deal_sizes,revenues
    
    
names,call_numbers,average_deal_sizes,revenues= cleanlines(lines)   
print("Name:",names)
print("Number of Calls:",call_numbers)
print("Average Deal Size:",average_deal_sizes)
print("Revenue:",revenues) 
    
#PERFORMANCE ANALYSIS REPORT
#Let’s start by determining how many employees we have. We can use the len function to check the length of a list . 

#So we have 11 employees.  

#We can define a list for their IDs ranging from 0 to 11 as we have 11 employees.    
print(len(names)) #11
IDs=list(range(0,11))
dictionary1=dict(zip(IDs,names))

dictionary2=dict(zip(revenues,names))   

#lowest and bests performances
sorted_dictionary=sorted(dictionary2)[0:3] #top 3 employee
for i in sorted_dictionary:
    print(dictionary2[i])
        
#besties
sorted_dictionary2=sorted(dictionary2,reverse=True)[0:3]
for i in sorted_dictionary2:
    print(dictionary2[i])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    