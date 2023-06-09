import numpy as np
a = np.arange(5)
print(a)
a[[1, 3, 4]] = 0
print(a)
b = np.arange(5)
print(b)
b[[0, 0, 2]] = [1, 2, 3]
print(b)
c = np.arange(5)
print(c)
c[[0, 0, 2]] += 1
print(c)