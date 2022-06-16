import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)
b = np.transpose(a)
print(b)
c = np.transpose(a, (1, 0))
print(c)

