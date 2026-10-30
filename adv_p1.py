import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Colored Scatterplots
iris = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Data Science\\MatplotLIB\\iris.csv')
iris['Species'] = iris['Species'].replace({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})
# print(iris) # cmap=winter summer jet ...etc

# # camp and alpha
# plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c=iris['Species'], cmap='jet', alpha=0.8 )
# plt.xlabel('Sepal Length')
# plt.ylabel('Petal Length')
# plt.colorbar()
# plt.show()

# # plot size
# plt.figure(figsize=(15.6, 7))
# plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c=iris['Species'], cmap='jet', alpha=0.8 )
# plt.xlabel('Sepal Length')
# plt.ylabel('Petal Length')
# plt.colorbar()
# plt.show()

# Annotations
better = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Data Science\\MatplotLIB\\batter.csv')
# sample_df = df.head(100).sample(25, random_state=5)
# print(sample_df)
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
plt.scatter(x, y)
plt.text(1,5,'Point 1')
plt.text(2,6,'Point 2')
plt.text(3,7,'Point 3')
plt.text(4,8,'Point 4', fontdict={'size':12, 'color':'brown'})
# horizontalline and verticalline
plt.axhline(2, color='black')
plt.axvline(2, color='black')
plt.show()