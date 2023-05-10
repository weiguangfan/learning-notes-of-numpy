import numpy as np
a = np.arange(24).reshape(2,3,4)
print(a.shape)
# (2, 3, 4)
print(a)
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
"""
print(a[1:, -2:, :-1])
"""
[[[16 17 18]
  [20 21 22]]]
"""
print(a[1])
"""
[[12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
"""
print(a[1, :, :])
"""
[[12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
"""
print(a[1] == a[1, :, :])
"""
[[ True  True  True  True]
 [ True  True  True  True]
 [ True  True  True  True]]
"""