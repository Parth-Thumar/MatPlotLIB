import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pie chart
# Univariate/Bivariate Analysis
# Categorical vs numerical
# Use case - To find contibution on a standard scale

# # simple data
# data = [12, 45, 100, 20, 49]
# subject = ['eng', 'math', 'physics', 'hindi', 'sst']
# plt.pie(data, labels=subject)
# plt.show()

# dataset
df = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\MatplotLIB\\gayle-175.csv')
# plt.pie(df['batsman_runs'], labels=df['batsman'], autopct='%0.1f%%')
# plt.show()

# # percentage and color
# plt.pie(df['batsman_runs'], labels=df['batsman'], autopct='%0.1f%%', colors=['tan', 'green', 'yellow', 'pink', 'cyan', 'lime'])
# plt.show()

# # explode shadow
# plt.pie(df['batsman_runs'], labels=df['batsman'], autopct='%0.1f%%', explode=[0.1, 0, 0.3, 0, 0, 0.1], shadow=True)
# plt.show()

# changing styles
arr = np.load('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\MatplotLIB\\big-array.npy')
plt.hist(arr, bins=[10, 20, 30, 40, 50, 60, 70], log=True)
# plt.style.use('fivethirtyeight')
plt.style.use('dark_background')
plt.show()
plt.savefig('sample.png')