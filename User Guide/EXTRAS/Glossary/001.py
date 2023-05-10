import numpy as np

# print(np.arange(24).reshape(2, 3, 4))
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
"""
# print(np.arange(24).reshape(4, -1))
"""
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
"""
a = np.arange(24).reshape(2, 3, 4)
print(a[...].shape)
# (2, 3, 4)
print(a[..., 0].shape)
# (2, 3)
print(a[0, ...].shape)
# (3, 4)
print(a[0, ..., 0].shape)
# (3,)