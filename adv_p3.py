import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 3D graph plots

# Scatter Plots
batters = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Advance MatplotLIB\\batter (1).csv')

# fig = plt.figure()
# ax = plt.subplot(projection='3d')
# ax.scatter3D(batters['runs'], batters['avg'], batters['strike_rate'])
# ax.set_title('IPL batsman analysis')
# ax.set_xlabel('Runs')
# ax.set_ylabel('Avg')
# ax.set_zlabel('Strike rate')
# fig.show()
# plt.show()

# Line plot

# x = [0, 1, 5, 25]
# y = [0, 10, 13, 0]
# z = [0, 13, 20, 9]

# fig = plt.figure()
# ax = plt.subplot(projection='3d')
# ax.scatter3D(x, y, z, s=[100, 100, 100, 100])
# ax.plot3D(x,y,z,color='red')
# fig.show()
# plt.show()

# Surface Plots

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
xx, yy = np.meshgrid(x, y)
# z = xx**2 + yy**2
# fig = plt.figure(figsize=(12, 8))
# ax = plt.subplot(projection='3d')
# p = ax.plot_surface(xx, yy, z, cmap='viridis')
# fig.colorbar(p)
# fig.show()
# plt.show()

# z = np.sin(xx) + np.cos(yy)
# fig = plt.figure(figsize=(12, 8))
# ax = plt.subplot(projection='3d')
# p = ax.plot_surface(xx, yy, z, cmap='viridis')
# fig.colorbar(p)
# fig.show()
# plt.show()

# z = np.sin(xx) + np.log(yy)
# fig = plt.figure(figsize=(12, 8))
# ax = plt.subplot(projection='3d')
# p = ax.plot_surface(xx, yy, z, cmap='viridis')
# fig.colorbar(p)
# fig.show()
# plt.show()

# Contour Plots

# z = xx**2 + yy**2
# fig = plt.figure(figsize=(12, 8))
# ax = plt.subplot()
# p = ax.contour(xx, yy, z, cmap='viridis')
# fig.colorbar(p)
# fig.show()
# plt.show()

# z = xx**2 + yy**2
# fig = plt.figure(figsize=(12, 8))
# ax = plt.subplot()
# p = ax.contourf(xx, yy, z, cmap='viridis')
# fig.colorbar(p)
# fig.show()
# plt.show()

# Heatmap
delivery = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Advance MatplotLIB\\IPL_Ball_by_Ball_2008_2022.csv')
# print(delivery.head())

temp_df = delivery[(delivery['ballnumber'].isin([1,2,3,4,5,6])) & (delivery['batsman_run']==6)]
grid = temp_df.pivot_table(index='overs', columns='ballnumber', values='batsman_run', aggfunc='count')
# print(grid)

plt.imshow(grid)
plt.colorbar()
plt.yticks(delivery['overs'].unique(), list(range(1,21)))
plt.xticks(np.arange(0,6), list(range(1,7)))
plt.show()