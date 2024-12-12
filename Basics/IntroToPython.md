type() tells you the type of variable a variable is

Different type = different behaviour

# Create a variable half

half = 0.5
# Create a variable intro

intro = "Hello! How are you?"
# Create a variable is_good
is_good = True

float = real numbers
int = integer numbers
str = sttring, text
bool = True, False

list [a, b ,c]

lists can contain many types of variables,
lists can also contain other lists

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas

areas = [hall, kit, liv, bed, bath]
# Print areas
print(areas)

Python uses 0 indexing, so the first element in a list
is 0.

Also, list slicing is confusing since it works the following way:
[start : end]
inclusive : exclusive

that means if i print areas[1:3], it'll only print
kit and liv

if i print areas[:4]
it'll print 
hall, kit, liv

if i print areas[3:]
it'll print 
bed and bath


to update an element within a list you do 

areas[0] = studio
this will change hall to studio

areas[0:2] = ["studio", 1.99]

this will change hall to studio and kit to 1.99

to add elementsto a list, you do
areas + [basketballcourt]

or

more_areas = areas + [basketballcourt]

to delete you do

del areas[1]

it will delete kit

to create an explicit list of a variable
you have to use

areas_updated = list(areas)

this way, when you edit areas, areas_updated
remains unchanged

FUNCTIONS

max() gives you the highest value of a list

tallest = max(fam)

tallest

round() rounds up a float to whichever decimal point you indicate
so, if you do round(1.68, 1) 
this will equal 1.7
if you do not specify, it will round up to the first decimal point
round(1.68)
will equal
2

help() gives you a guide of a command

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

#print() prints something
#type() tells you the type of variable
#str() converts something to a string
#int() converts something to an integer
#float(), well, pretty obvious

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, key=None, reverse=True)

# Print out full_sorted
print(full_sorted)

in python everything is an object
and objects have specific methods associated to them 
depending on type

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size

areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)



NumPy

you cannot do operations between lists
so you import numpy to use arrays, thus
it will allow you to do calculates between 
variables which have lists assigned

but if you wanna do calculations between arrays
they must contain  single object type

an array is a new kind of python type like
floats or integers


# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m

print(np_height_m)


import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])


avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))


Finished course in DataCamp: Intro to Python 12/12/2024










