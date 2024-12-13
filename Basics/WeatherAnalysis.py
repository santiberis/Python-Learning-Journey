#First personal project analyzing a randomly generated dataset by ChatGPT, the purpose is to consolidate concepts learned throughout the Beginner and Intermediate courses on DataCamp

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#This is how you import a csv
df = pd.read_csv("weatherville_data.csv")

#this will show you the first 5 and last 5 rows of the dataset
print(df)

#This will show you the entire dataset in a string
# print(df.to_string())

#this checks if there are any missing values in the dataset
print(df.isna().sum())

#this returns either true or false if there are missing values
print(df.isna().any().any())

#Calculating averages of each column of the dataframe
avg_temp = np.mean(df["Temperature (°C)"])
print("Average yearly temperature in °C:", avg_temp)

avg_rain = np.mean(df.iloc[:, 2])
print("Average yearly rain in mm:", avg_rain)

avg_humidity = np.mean(df["Humidity (%)"])
print("Average yearly humidity in (%):",  avg_humidity)


#Calculating minimums and maximums of each column of the dataframe
max_humidity=max(df["Humidity (%)"])
print("The maximum humidity throughout the year was:", max_humidity)

min_humidity=min(df["Humidity (%)"])
print("The minimum humidity throughout the year was:", min_humidity)

max_temp = max(df["Temperature (°C)"])
print("The maximum temperature throughout the year was:", max_temp)

min_temp = min(df["Temperature (°C)"])
print("The minimum temperature throughout the year was:", min_temp)

max_rain = max(df.iloc[:, 2])
print("The maximum rain throughout the year was:", max_rain)


min_rain = min(df.iloc[:, 2])
print("The minimum rain throughout the year was:", min_rain)


#Grouping rows according to season
groupBySeason = (df.groupby(["Season"]))

print(groupBySeason.count())

#Calculating averages per column based on season
avg_temp_by_season = groupBySeason["Temperature (°C)"].mean()
print("The average temperature per season is:", avg_temp_by_season)

avg_rain_by_season = groupBySeason["Rainfall (mm)"].mean()
print("The average rainfall per season is:", avg_rain_by_season)

avg_humidity_by_season = groupBySeason["Humidity (%)"].mean()
print("The average humidity per season is:", avg_humidity_by_season)

print("The season with the highest average temperature is Autumn")

print("The season with the highest average rainfall is Summer")

print("The season with the highest average humidity is Summer")


#Visualizing each column
plt.plot(df["Temperature (°C)"])

plt.show()

plt.hist(df["Rainfall (mm)"])
plt.show()

humidity = df["Humidity (%)"]
temperature = df["Temperature (°C)"]
plt.scatter(temperature, humidity)
plt.show()


print("The best season for outdoor activities is Autumn, since it has the highest average temperature, lowest average rainfall and lowest humidity among all seasons")

print("The season that needs the most preparation for rainfall is Summer, since it has highest average rainfall in (mm)")

"""
OBSERVATIONS AND ROOM FOR IMPROVEMENT:
1)
Enhanced Reporting
Write the results (averages, min/max, etc.) to a text file for documentation:
with open("report.txt", "w") as f:
    f.write(f"Average Yearly Temperature: {avg_temp}\n")

2)
 Identify the season with:
Maximum average temperature.
Maximum total rainfall.
Example:
season_max_rain = df.groupby("Season")["Rainfall (mm)"].sum().idxmax()
print(f"Season with most rainfall: {season_max_rain}")

3)
Add visualizations for better data communication:
Temperature trends over time:
plt.plot(df["Date"], df["Temperature (°C)"])
plt.title("Temperature Trends")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()

4)
Perform correlation analysis between columns:
print(df.corr())

5)
Add columns for:
Daily Temperature Difference:
df["Temp Difference"] = df["Temperature (°C)"].diff()
Cumulative Rainfall:
df["Cumulative Rainfall"] = df["Rainfall (mm)"].cumsum()

"""