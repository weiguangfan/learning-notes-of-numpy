import numpy as np
rg = np.random.default_rng(1)
print(rg)
print(type(rg))
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
print(a)
print(a.dtype)
print(b)
print(b.dtype)
a *= 3
print(a)
b += a
print(b)