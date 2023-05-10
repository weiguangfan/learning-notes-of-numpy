import numpy as np
rng = np.random.default_rng()
print(rng)
# Generator(PCG64)
print(rng.random())
# 0.7625978762973333
print(type(rng.random()))
# <class 'float'>
print(rng.random((5,)))
# [0.29842778 0.31431391 0.74589244 0.15385792 0.09743928]
print(type(rng.random((5,))))
# <class 'numpy.ndarray'>
print((5 * rng.random((3, 2)) - 5))
"""
[[-1.48121189 -0.96213459]
 [-2.90831731 -1.7286697 ]
 [-3.21461171 -0.76010003]]
"""