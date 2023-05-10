import numpy as np
dt = np.dtype('>i4')
print(dt)
# >i4
print(dt.byteorder)
# >
print(dt.itemsize)
# 4
print(dt.name)
# int32
print(dt.type is np.int32)
# True
