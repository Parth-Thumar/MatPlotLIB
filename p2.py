import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Scatter Plotes
# Bivariate Analysis
# numerical vs numerical
# Use case - Finding correlation

# plt.sctter simple function
x = np.linspace(-10, 10, 50)
y = 10*x + 3 + np.random.randint(0, 300, 50)
# plt.scatter(x, y)
# plt.show()

# plt.scatter in pandas data
# slower
df = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\MatplotLIB\\batter.csv')
df = df.head(50)
# print(df)
# plt.scatter(df['avg'], df['strike_rate'], color='black', marker='+')
# plt.title('Avg and SR analysis of Top 50 Batsman')
# plt.xlabel('Average')
# plt.ylabel('Strike Rate')
# plt.show()

# size
tips = sns.load_dataset('tips')
# plt.scatter(tips['total_bill'], tips['tip'], s=tips['size']*10)
# plt.show()

# scatterplot using plt.plot
# faster
plt.plot(tips['total_bill'], tips['tip'], 'o')
plt.show()