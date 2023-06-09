import numpy as np
a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
print(a)
d = a.copy()
print(d)
print(d is a)
print(d.base is a)
d[0, 0] = 9999
print(d)
print(a)