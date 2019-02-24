
# coding: utf-8
import tensorflow as tf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

def minimumEditDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]
 
print(minimumEditDistance("kitten","sitting"))
print(minimumEditDistance("rosettacode","raisethysword"))

def levenshteinDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    lensum = float(m + n)
    d = []
    for i in range(m+1):
        d.append([i])
    del d[0][0]
    for j in range(n+1):
        d[0].append(j)
    for j in range(1,n+1):
        for i in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                d[i].insert(j,d[i-1][j-1])
            else:
                minimum = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+2)
                d[i].insert(j, minimum)
    ldist = d[-1][-1]
    ratio = (lensum - ldist)/lensum
    return [ldist, ratio]

print(levenshteinDistance("kitten","sitting"))
print(levenshteinDistance("rosettacode","raisethysword"))

arr = np.empty((0,4))

answers = ["y=3a+b", "y = 3a+b", "y=3a + b", "y = 3a + b", "y = 3 a + b", "y = b + 3a", "y = b+3a", "y = 5a + 6b", "y = 12a + 6b"]

for i, ith_item in enumerate(answers):
    for j, jth_item in enumerate(answers[i+1:]):
        d, r = levenshteinDistance(ith_item, jth_item)
        arr = np.append(arr, np.array([[i, j, d, r]]), axis=0)

print(arr)

df = pd.DataFrame({'i':arr[:,0], 'j':arr[:,1], 'distance':arr[:,2], 'ratio':arr[:,3]})
print(df)

plt.plot(df['distance'], df['i'], 'ro')
plt.show()
# plt.plot(df['j'], df['distance'], 'ro')
# plt.show()
# plt.plot(df['ratio'], 'ro')
# plt.show()
# plt.plot(arr)
# plt.show()

print(df['i'].values)
print(df['j'].values)
print(df['distance'].values)


# Axes3D.plot_trisurf(df['i'].values, df['j'].values, df['distance'].values)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(df['i'].values, df['j'].values, df['distance'].values, linewidth=0.2, antialiased=True)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['i'].values, df['j'].values, df['ratio'].values)
plt.show()

kmeans = KMeans(n_clusters=3, random_state=0).fit(arr)

