import numpy as np
x = np.arange(0, 10, 2)
print(x)
y = np.arange(5)
print(y)
m = np.vstack([x, y])
print(m)
xy = np.hstack([x, y])
print(xy)