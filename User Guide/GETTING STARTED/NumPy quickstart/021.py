import numpy as np
from numpy import newaxis
# rg = np.random.default_rng(1)
# print(rg)
# a = np.floor(10 * rg.random((2, 2)))
# print(a)
# b = np.floor(10 * rg.random((2, 2)))
# print(b)
#
# print(np.column_stack((a, b)))

a = np.array([4., 2.])
b = np.array([3., 8.])
print(a)
print(a.shape)
print(b)
print(b.shape)
# print(np.column_stack((a, b)))
# print(np.hstack((a, b)))

# print(a[:, newaxis])
# print(a[:, newaxis].shape)
# print(b[:, newaxis])
# print(b[:, newaxis].shape)
# print(a[:, newaxis, newaxis])
# print(a[:, newaxis, newaxis].shape)
# print(b[:, newaxis, newaxis])
# print(b[:, newaxis, newaxis].shape)
# print(np.column_stack((a[:, newaxis], b[:, newaxis])))
# print(np.hstack((a[:, newaxis], b[:, newaxis])))

# print(np.row_stack is np.vstack)
# print(np.column_stack is np.hstack)

# print(np.concatenate((a, b), axis=0))
# print(np.concatenate((a, b), axis=1))


print(np.r_[1:4, 0, 4])