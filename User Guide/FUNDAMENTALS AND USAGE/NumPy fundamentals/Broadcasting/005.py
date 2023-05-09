"""
For example, if a.shape is (5,1), b.shape is (1,6), c.shape is (6,) and d.shape is () so that d is a scalar, then a, b, c, and d are all broadcastable to dimension (5,6); and

a acts like a (5,6) array where a[:,0] is broadcast to the other columns,

b acts like a (5,6) array where b[0,:] is broadcast to the other rows,

c acts like a (1,6) array and therefore like a (5,6) array where c[:] is broadcast to every row, and finally,

d acts like a (5,6) array where the single value is repeated.
"""
import numpy as np
a1 = np.random.Generator.random(size=(5,4))
b1 = np.random.Generator.random(size=(1,))
print(a1 * b1)
a2 = np.random.Generator.random(size=(5,4))
b2 = np.random.Generator.random(size=(4,))
print(a2 * b2)
a3 = np.random.Generator.random(size=(15,3,5))
b3 = np.random.Generator.random(size=(15,1,5))
print(a3 * b3)
a4 = np.random.Generator.random(size=(15,3,5))
b4 = np.random.Generator.random(size=(3,5))
print(a4 * b4)
a5 = np.random.Generator.random(size=(15,3,5))
b5 = np.random.Generator.random(size=(3,1))
print(a5 * b5)
