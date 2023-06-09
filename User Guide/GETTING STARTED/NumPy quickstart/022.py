import numpy as np
rg = np.random.default_rng(1)
print(rg)
a = np.floor(10 * rg.random((2, 12)))
print(a)
print(np.hsplit(a, 3))
print(np.hsplit(a, (3, 4)))