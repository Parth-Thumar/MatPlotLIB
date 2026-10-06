# Types of Data

# Numerical Data
# Categorical Data

# import the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2D plots
# Bivariate Analysis
# categorical -> numerical and numerical -> numerical
# Use case - Time series data

# # plotting a simple function x axis -> categorical data y axis -> numerical data
# price = [48000, 54000, 57000, 49000, 47000, 45000]
# year = [2015, 2016, 2017, 2018, 2019, 2020]
# plt.plot(year, price)
# plt.show()

# from a pandas dataframe
batsman = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\MatplotLIB\\sharma-kohli.csv')
# print(batsman)
# plt.plot(batsman['index'], batsman['V Kohli'])
# plt.show()

# # plotting multiple plots
# plt.plot(batsman['index'], batsman['V Kohli'])
# plt.plot(batsman['index'], batsman['RG Sharma'])
# plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
# plt.xlabel('Seasons')
# plt.ylabel('Runs Scored')
# plt.show()

# labels title

# # colors(hex) and line(width and style) and marker(size) uses has code
# plt.plot(batsman['index'], batsman['V Kohli'], color='green')
# plt.plot(batsman['index'], batsman['RG Sharma'], color='black')
# plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
# plt.xlabel('Seasons')
# plt.ylabel('Runs Scored')
# plt.show()

# # linestyle dashed dotted solid dashdot
# # Use width
# # marker + . < > D O 
# plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='solid', linewidth=3, marker='D', markersize=10)
# plt.plot(batsman['index'], batsman['RG Sharma'], color='black', linestyle='dashdot', linewidth=5, marker='+')
# plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
# plt.xlabel('Seasons')
# plt.ylabel('Runs Scored')
# plt.show()

# # legend -> location
# plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='solid', linewidth=3, marker='D', markersize=10, label='Virat')
# plt.plot(batsman['index'], batsman['RG Sharma'], color='black', linestyle='dashdot', linewidth=5, marker='+', label='Rohit')
# plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
# plt.xlabel('Seasons')
# plt.ylabel('Runs Scored')
# plt.legend()
# plt.show()

# # limiting axes
# price = [48000, 54000, 57000, 49000, 47000, 45000, 450000]
# year = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
# plt.plot(year, price)
# plt.ylim(0, 75000)
# plt.xlim(2017, 2019)
# plt.show()

# grid
plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='solid', linewidth=3, marker='D', markersize=10, label='Virat')
plt.plot(batsman['index'], batsman['RG Sharma'], color='black', linestyle='dashdot', linewidth=5, marker='+', label='Rohit')
plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
plt.xlabel('Seasons')
plt.ylabel('Runs Scored')
plt.legend()
plt.grid()
plt.show()