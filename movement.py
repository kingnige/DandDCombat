import numpy as np

#create an array to hold the information
n = 11
m = 11
a = [0] * n
for i in range(n):
    a[i] = [0] * m
print(np.matrix(a))