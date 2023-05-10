import numpy as np
rng = np.random.default_rng(12345)
print(rng)
# Generator(PCG64)
rints = rng.integers(low=0,high=10,size=3)
print(rints)
# [6 2 7]
print(type(rints[0]))
# <class 'numpy.int64'>