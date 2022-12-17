#sort the provided list into different data types

from collections import defaultdict

Data_list = [1,2,3,4,'Python','Internship','Session1',True,21,False,[1,4,5], 7.4, 1.2]

print("The original list : " + str(Data_list))

result = defaultdict(list)
for a in Data_list:
    result[type(a)].append(a)

types = [int, str, bool, range, dict, list, complex, float, tuple]
for y in types:
    if len(result[y]) != 0:
        print(result[y])
