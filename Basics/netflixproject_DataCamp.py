# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
import matplotlib.pyplot as plt
import numpy as np  # Added import for numpy

netflix_df = netflix_df[netflix_df["release_year"] >= 1990]
duration_1 = (netflix_df["duration"])

plt.hist(duration_1, bins=50)
plt.xlabel("duration")
plt.ylabel("count")
plt.show()

# Fixed the print statement by closing the parenthesis
print("The most common duration for a movie within the 90s decade, was: 93, repeated: " + str((netflix_df["duration"] == 93).sum()), "times")
duration = 100
short_movie_count = 0
for duration in netflix_df["duration"]:
    if duration <= 90:
        short_movie_count += 1
    else: 1
        
print(short_movie_count)
        
print(f"Number of short movies (<= 90 minutes): {short_movie_count}")
short_movies_df = netflix_df[netflix_df["duration"] <= 90]