import numpy as np
from numpy import pi
a = np.ones(3, dtype=np.int32)
print(a)
print(a.dtype)
b = np.linspace(0,pi,3)
print(b)
print(b.dtype.name)
c = a + b
print(c)
print(c.dtype)
print(c.dtype.name)
d = np.exp(c * 1j)
print(d)
print(d.dtype)