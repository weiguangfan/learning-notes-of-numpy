import numpy as np
a = np.arange(int(1e8))
print(a)
b = a[:100].copy()
print(b)
del a
print(b)