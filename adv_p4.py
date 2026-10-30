import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas plot()

# # on series
# s = pd.Series([1,2,3,4,5,6,7])
# s.plot(kind='line')
# plt.show()

# can be used on a dataframe as well

import seaborn as sns
tips = sns.load_dataset('tips')

# scatter plot -> label -> markers -> figsize -> color -> cmap
tips['size'] = tips['size'] * 100
# tips.plot(kind='scatter', x='total_bill', y='tip', title='Cost Analysis', c='sex', cmap='viridis', marker='+', figsize=(10,6), s='size')
# plt.show()

# bar chart -> single -> horizontal -> multiple
# usind tips
temp = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Advance MatplotLIB\\batsman_season_record (1).csv')
# tips.plot(kind='bar',x='sex',y='total_bill')
# plt.show()

# temp['2015'].plot(kind='bar')
# plt.show()3

# tips.groupby('sex')['total_bill'].mean().plot(kind='bar')

# # stacked bar chart
# temp.plot(kind='bar', stacked=True)
# plt.show()

# # histogram 
# # using stocks
# stocks = sns.load_dataset('stocks')
# stocks[['MSFT', 'FB']].plot(kind='hist', bins=40)
# plt.show()

# pie -> single and multiple 
df = pd.DataFrame(
    {
        'batsman': ['Dhawan', 'Rohit', 'Virat', 'SKY', 'Pandya', 'Pant'],
        'match1': [120, 90, 35, 45, 12, 10],
        'match2': [0, 1, 123, 130, 34, 45],
        'match3': [50, 24, 145, 45, 10, 90]
    }
)
# df['match1'].plot(kind='pie', labels=df['batsman'].values, autopct='%0.1f%%')
# plt.show()

# # multiple pie chart
# df[['match1', 'match2', 'match3']].plot(kind='pie', subplots=True, figsize=(15,8))
# plt.show()

# on multiple dataframe
# using tips
tips.pivot_table(index=['day','time'], columns=['sex','smoker'], values='total_bill', aggfunc='mean').plot(kind='pie', subplots=True, figsize=(20,10))
plt.show()