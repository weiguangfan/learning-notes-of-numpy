import numpy as np
rg = np.random.default_rng(1)
print(rg)
a = np.floor(10 * rg.random((2, 12)))
print(a)
# print(np.hsplit(a, 3))
# print(np.hsplit(a, (3, 4)))
# print(np.vsplit(a, 2))
# print(np.array_split(a, 3, axis=1))
print(np.array_split(a, 2, axis=0))