import numpy as np
x = np.arange(10)
print(x)
# [0 1 2 3 4 5 6 7 8 9]
print(x[2])
# 2
print(x[-2])
# 8
x.shape = (2,5)
print(x)
"""
[[0 1 2 3 4]
 [5 6 7 8 9]]
"""
print(x[1, 3])
# 8
print(x[1, -1])
# 9
print(x[0])
# [0 1 2 3 4]
print(x[0][2])
# 2




