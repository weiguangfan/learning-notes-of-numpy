import numpy as np
a = np.arange(12).reshape(3,4)
print(a)
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""
print(np.flip(a, axis=0))
"""
[[ 8  9 10 11]
 [ 4  5  6  7]
 [ 0  1  2  3]]
"""
print(np.array((a[0, :], a[1, :], a[2, :])))
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""
print(np.array((a[2,:],a[1,:],a[0,:])))
"""
[[ 8  9 10 11]
 [ 4  5  6  7]
 [ 0  1  2  3]]
"""