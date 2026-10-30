import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# A different way to plot graphs
batters = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Advance MatplotLIB\\batter (1).csv')

c = batters.head(100).sample(25)
# plt.figure(figsize=(15,12))
# plt.scatter(c['avg'],c['strike_rate'],s=c['runs'])#s=size
# plt.axhline(130,color='red')
# plt.axvline(40,color='red')#line of horizontal and vertical of you needed
# for i in range(c.shape[0]):
#     plt.text(c['avg'].values[i],c['strike_rate'].values[i],c['batter'].values[i])
# plt.show()

# # plt.scatter(batters['avg'], batters['strike_rate'])
# fig,ax = plt.subplots(figsize=(15,6))
# ax.scatter(batters['avg'], batters['strike_rate'], color='red', marker='+')
# ax.set_title('Somthing')
# ax.set_xlabel('Avg')
# ax.set_ylabel('Strike Rate')
# fig.show()
# plt.show()

# fig,ax = plt.subplots(nrows=2,ncols=1)#2*1=2 graph or 2*2=4 graph
# ax[0].scatter(batters['avg'],batters['strike_rate'], color='black')
# ax[1].scatter(batters['avg'],batters['runs'])
# ax[0].set_title('something')#ax[0] is first graph]
# ax[0].set_xlabel('avg')
# fig.show()
# plt.show()

# fig,ax = plt.subplots(nrows=2,ncols=2, figsize=(10,10))#2*1=2 graph or 2*2=4 graph

# ax[0,0].scatter(batters['avg'],batters['strike_rate'], color='black')
# ax[0,1].scatter(batters['avg'],batters['runs'])
# ax[1,0].hist(batters['avg'])
# ax[1,1].hist(batters['runs'])

# ax[0,0].set_title('Avg vs Strike rate')#ax[0] is first graph]
# ax[0,0].set_ylabel('Strike rate')
# ax[0,1].set_title('Avg vs Runs')
# ax[0,1].set_ylabel('Runs')
# ax[0,1].set_xlabel('Avg')

# fig.show()
# plt.show()

# fig = plt.figure()
# ax1.scatter(batters['avg'], batters['strike_rate'], color='skyblue')
# ax2 = fig.add_subplot(2, 1, 2)
# ax2.hist(batters['runs'])
# fig.show()
# plt.show()