import numpy as np
c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [ 10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
print(c)
print(c.shape)
print(c[1, ...])
print(c[..., 2])