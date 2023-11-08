import numpy as np
v1 = np.array([1,2,3])
v2 = np.array([4,7,5])
print(np.dot(v1, v2))
v3 = np.mat([1,2,3])
v4 = np.mat([4,7,5])
print(np.multiply(v3, v4))
print(np.sum(np.multiply(v3, v4)))

np.nonzero()