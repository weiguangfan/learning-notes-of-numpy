import numpy as np
rng = np.random.default_rng(12345)
print(rng)
# Generator(PCG64)
rfloat = rng.random()
print(rfloat)
# 0.22733602246716966
print(type(rfloat))
# <class 'float'>