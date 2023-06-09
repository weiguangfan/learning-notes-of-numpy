import numpy as np
a = np.arange(30)
print(a)
b = a.reshape((2, -1, 3))
print(b)
print(b.shape)
