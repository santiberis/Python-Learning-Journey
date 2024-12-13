list1 = list([10, 20, 30, 40, 50])

print(list1)
list.reverse(list1)
print(list1)

list2 = list([1, 2, 3])

list3 = list([4, 5 , 6])

print(list2 + list3)

my_list = list([10, 20, 30, 40, 50, 60, 70, 80])

my_list1 = my_list[0:3]
my_list2 = my_list[5:8]
print(my_list1, my_list2)

import numpy as np

new_list = np.array([2, 4, 6, 8])

print(new_list * 3)

new_list1 = list([1, 2, 2, 3, 4, 4, 5])
print(new_list1)
new_list2 = list(set(new_list1))
print(new_list2)

dictionary = {1:"apple", 2:"banana", 3:"cherry"}
print(dictionary)

dictionary[4] = "date"
print(dictionary)

dictionary1 = {1:"apple", 2:"banana"}
dictionary2 = {3:"cherry", 4:"date"}

# print(dictionary1 + dictionary2)

dictionary3 = {1:"apple", 2:"banana", 3:"cherry"}
print(dictionary3)
del(dictionary3[2])
print(dictionary3)

array = np.array([1, 2, 3, 4, 5])
print(array)

array2 = np.array([10, 20, 30])
print(array2)
array2 = array2 * 2
print(array2)

array = np.array([1, 2, 3, 4, 5])

print(array[0:3])
print(array[3:6])

array2 = np.array([10, 20, 30, 40, 50])

print(np.mean(array2))
print(np.sum(array2))

array4 = np.array([1, 2, 3, 4, 5,6])

#dont know how to reshape it
# import pandas as pd
# dataframe1 = pd.DataFrame([["Name" ]["Age"]])
# print(dataframe1)
#cant create the dataframe


#RETRAINING ON EXCERCISES WHERE FOUND DIFFICULTY

list42 = [1,2,3,4,5,6,7,8,9,10]
list43 = [2,4,6,8,10]

list44 = [1, 2,3,2,4,2,5]
print(list44.count(2))

nested_dict = {
    'fruits': {'apple': 5, 'banana': 10},
    'vegetables': {'carrot': 7, 'spinach': 3}
}

# print(nested_dict[["vegetables"], ["carrot"]])

del(nested_dict["banana"])