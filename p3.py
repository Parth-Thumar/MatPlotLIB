import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# bar
# Bivariate Analysis
# Numerical vs Categorical
# Use case - Aggregate analysis of groups

# simple bar chart
children = [10, 20, 40, 10, 30]
colors = ['red', 'blue', 'green', 'yellow', 'pink']
# plt.bar(colors, children, color='pink')
# plt.show() # this is vertical chart

# bar chart using data

# # horizontal chart
# plt.barh(colors, children, color='pink')
# plt.show()

# color and label
df = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\MatplotLIB\\batsman_season_record.csv')
# print(df)
# plt.bar(np.arange(df.shape[0]) - 0.2, df['2015'], width=0.2, color='green')
# plt.bar(np.arange(df.shape[0]), df['2016'], width=0.2, color='skyblue')
# plt.bar(np.arange(df.shape[0]) + 0.2, df['2017'], width=0.2, color='blue')
# plt.xticks(np.arange(df.shape[0]), df['batsman'])
# plt.show()

# Multiple Bar charts
# xticks

# # a problem
# children = [10, 20, 40, 10, 30]
# colors = ['red red red red', 'blue blue blue blue', 'green green green green', 'yellow yellow yellow yellow', 'pink pink pink pink']
# plt.bar(colors,children,color='black')
# plt.xticks(rotation='vertical')
# plt.show()

# Stacked Bar chart
plt.bar(df['batsman'], df['2017'], label='2017')
plt.bar(df['batsman'], df['2016'], bottom=df['2017'], label='2016')
plt.bar(df['batsman'], df['2015'], bottom=(df['2016'] + df['2017']), label='2015')
plt.legend()
plt.show()