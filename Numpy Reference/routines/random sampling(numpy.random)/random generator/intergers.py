import numpy as np
rng = np.random.default_rng()
print(rng)
# Generator(PCG64)
print(rng.integers(2, size=10))
# [1 0 0 1 0 0 0 1 0 1]
print(rng.integers(1, size=10))
# [0 0 0 0 0 0 0 0 0 0]
print(rng.integers(5, size=(2, 4)))
"""
[[0 2 2 1]
 [2 3 4 1]]
"""
print(rng.integers(1, [3, 5, 9]))
# [2 1 2]
print(rng.integers([1, 5, 7], 10))
# [9 6 8]
print(rng.integers([1, 3, 5, 7], [[10], [20]], dtype=np.uint8))
"""
[[ 1  9  8  9]
 [ 9  7 10 10]]
"""