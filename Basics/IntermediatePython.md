# Print the last item from year and pop

print(len(year))
print(len(pop))
print(year[-1])
print(year.count)
print(pop.count)
print(pop[-1])
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()


# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
#logarithmic scales help us "standardize" info in a visual way
plt.xscale("log")

# Show plot
plt.show()


#histograms help us see frequency in a much more efficient way

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()


# Build histogram with 5 bins
plt.hist(life_exp, bins = 5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clean up again
plt.show()
#plt.clf() cleans whichever hists where created up to  that point in the script


#Histograms are the best for distribution
#Scatter plots are best for correlation


#CUSTOMIZING PLOTS

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)


# Add title
plt.title(title)

# After customizing, display the plot
plt.show()

# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

plt.yticks(tick_val, tick_lab)
# Adapt the ticks on the x-axis

plt.xticks(tick_val, tick_lab)
# After customizing, display the plot
plt.show()

# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop

np_pop = np.array(pop)
# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

#DICTIONARIES
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 'france':"paris","germany":"berlin","norway":"oslo"}

# Print europe
print(europe)


# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe["norway"])



# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe["italy"] = "rome"

# Print out italy in europe
print("italy" in europe)
#This returns true, since its a way to verify if changes were made

# Add poland to europe
europe["poland"] = "warsaw"
# Print europe
print(europe)



# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe["germany"] = "berlin"

# Remove australia
del(europe["australia"])

# Print europe
print(europe)

#CREATING DICTIONARIES AND SUBDICTIONARIES

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
europe["france"]["capital"]

# Create sub-dictionary data
data = {
    "capital":"rome",
    "population":59.83,
}

# Add data to europe under key 'italy'
europe["italy"] = data

# Print europe
print(europe)



# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country":names,
        "drives_right":dr,
        "cars_per_cap":cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels 


# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)


#pandas dataframes

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars["country"])

# Print out country column as Pandas DataFrame
print(cars[["country"]])

# Print out DataFrame with country and drives_right columns
print(cars[["country", "drives_right"]])


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars)
print(cars.loc["MOR", "drives_right"])
# Print sub-DataFrame
print(cars.loc[["RU", "MOR"], ["country", "drives_right"]])


#PAY SPECIAL NOTE TO THIS CAUSE IT COSTED ME

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Print out drives_right column as Series
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.iloc[:, [0, 2]])


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner

sel = cars[cars["drives_right"]]

# Print sel
print(sel)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]

many_cars = cpc > 500

car_maniac = cars[many_cars]
# Print car_maniac
print(car_maniac)

script.py
123456781011121314915
# Import cars dataimport pandas as pdcars = pd.read_csv('cars.csv', index_col = 0)# Import numpy, you'll need thisimport numpy as np# Create medium: observations with cars_per_cap between 100 and 500between = np.logical_and(cpc > 100, cpc < 500)medium = cars[between]# Print mediumcpc = cars["cars_per_cap"]print(medium)

IPython Shell
Slides
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars["cars_per_cap"]
medium = np.logical_and(cpc > 100, cpc < 500)



# Print medium
print(medium)
US     False
AUS    False
JPN    False
IN     False
RU      True
MOR    False
EG     False
Name: cars_per_cap, dtype: bool

<script.py> output:
    US     False
    AUS    False
    JPN    False
    IN     False
    RU      True
    MOR    False
    EG     False
    Name: cars_per_cap, dtype: bool

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars["cars_per_cap"]
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]


# Print medium
print(medium)

    cars_per_cap country  drives_right
RU           200  Russia          True


# Initialize offset
offset=8



# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)

correcting...
7
correcting...
6
correcting...
5
correcting...
4
correcting...
3
correcting...
2
correcting...
1
correcting...
0


# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset + 1    
    print(offset)

<script.py> output:
    correcting...
    -5
    correcting...
    -4
    correcting...
    -3
    correcting...
    -2
    correcting...
    -1
    correcti
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for rooms in areas:
    print(rooms)

<script.py> output:
    11.25
    18.0
    20.0
    10.75
    9.5


# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas):
    print("room " + str(index) + ": " + str(area))


<script.py> output:
    room 0: 11.25
    room 1: 18.0
    room 2: 20.0
    room 3: 10.75
    room 4: 9.5
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for room in house:
    print("the " + room[0] + " is " + str(room[1]) + " sqm")
