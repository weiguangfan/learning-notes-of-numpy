import numpy as np
b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum(axis=0))
print(b.min(axis=1))
print(b.cumsum(axis=1))