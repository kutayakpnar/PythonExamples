
with open("employee_revenue.txt","r+",encoding="utf-8") as file:
    data=file.read()
    lines=data.splitlines()
    """string=lines[0]
    string=string.strip(" ")
    string=string.lower()
    string=string.capitalize()
    split_string=string.split(" ")

    name = split_string[0]
    call_number=split_string[2]

    for i in split_string:

        if "$" in i:
            average_deal_size=i.split("$")[0]

    dollars_index=split_string.index("dollars")
    revenue_index=dollars_index-1
    revenue=split_string[revenue_index]

print("Name:",name)
print("Numer of calls:",call_number)
print("Average Deasl Size:",average_deal_size)
print("Revenue:",revenue)
average_deal_size=int(average_deal_size)
call_number=int(call_number)
revenue=int(revenue)"""
    names=[]
    call_numbers=[]
    average_deal_sizes=[]
    revenues=[]
    def clean_extract(lines):
        for employee in lines:
            employee=employee.strip(" ")
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
            revenue=int(revenue)

            names.append(name)
            call_numbers.append(call_number)
            average_deal_sizes.append(average_deal_size)
            revenues.append(revenue)

        return names,call_numbers,average_deal_sizes,revenues

    clean_extract(lines)
print("Names:",names)
print("Number of calls:",call_numbers)
print("Average deal size:",average_deal_sizes)
print("Revenues:",revenues)

print(len(names))
IDs=list(range(0,11))
print(IDs)

dictionary1=dict(zip(IDs,names))
print(dictionary1)
dictionary2=dict(zip(revenues,names))
print(dictionary2)

sorted_dictionary=sorted(dictionary2)[0:3]
for i in sorted_dictionary:                    #finding lowest revenues
    print(dictionary2[i])

sorted_dictionary2=sorted(dictionary2,reverse=True)[0:3]
for i in sorted_dictionary2:
    print(dictionary2[i])

