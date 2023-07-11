import numpy as np
a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
print(a)
# c = a.view()
# print(c)
# print(c is a)
# print(c.base is a)
# print(c.flags.owndata)
# c = c.reshape((2, 6))
# print(c)
# print(a.shape)
# c[0, 4] = 1234
# print(c)
# print(a)
s = a[:, 1:3]
print(s)
s[:] = 10
print(s)
print(a)