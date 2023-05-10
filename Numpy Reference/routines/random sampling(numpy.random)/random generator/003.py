import numpy as np
rng = np.random.default_rng(seed=42)
print(rng)
# Generator(PCG64)
arr1 = rng.random((3,3))
print(arr1)
"""
[[0.77395605 0.43887844 0.85859792]
 [0.69736803 0.09417735 0.97562235]
 [0.7611397  0.78606431 0.12811363]]
"""