names_liste = ["Ben", "Omer", "Karen", "Celine", "Sue", "Bora", "Rose", "Ellen", "Bob", "Taylor", "Jude"]
Number_of_calls = [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
Average_deal_size = ['8', '6', '24', '32', '5', '25', '25', '40', '15', '10', '12']
Revenues = [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]


import numpy as np

data = np.array([], dtype=int)  # While creating arrays,


# we can define what kind of data we will have in the array with the dtype parameter.
def append_names(Names):
    global data
    for i in Names:
        data = np.append(data, Names.index(i))


def append_performance(feature_list):
    global data
    data = np.append(data, feature_list)


append_names(names_liste)
append_performance(Number_of_calls)
append_performance(Average_deal_size)
"""
append_performance(Revenues)
data = data.reshape(4, 11)
print(data)

print(data.shape)

print(data[0])  # ['0' '1' '2' '3' '4' '5' '6' '7' '8' '9' '10']
print(data[1])
print(data[2])

print(data[3, 7])  # 6000 ellens revenue


def calculate_performance(employeename):
    idx = names_liste.index(employeename)
    numberofcalls = data[1, idx]
    averagedealsize = data[2, idx]
    revenue = data[3, idx]

    score = (averagedealsize * revenue) / numberofcalls
    return score


print(calculate_performance("Karen"))"""
