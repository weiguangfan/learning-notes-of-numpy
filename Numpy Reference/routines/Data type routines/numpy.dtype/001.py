import numpy as np

print(np.dtype(np.int16))
# int16
print(type(np.dtype(np.int16)))
# <class 'numpy.dtype[int16]'>
print(np.dtype([('f1', np.int16)]))
# [('f1', '<i2')]
print(np.dtype([('f1', [('f1', np.int16)])]))
# [('f1', [('f1', '<i2')])]
print(np.dtype([('f1', np.uint64), ('f2', np.int32)]))
# [('f1', '<u8'), ('f2', '<i4')]
print(np.dtype([('a', 'f8'), ('b', 'S10')]))
# [('a', '<f8'), ('b', 'S10')]
print(np.dtype('i4,(2,3)f8'))
# [('f0', '<i4'), ('f1', '<f8', (2, 3))]
print(np.dtype([("hello", (np.int64, 3)), ('world', np.void, 10)]))
# [('hello', '<i8', (3,)), ('world', 'V10')]
print(np.dtype((np.int16, {'x': (np.int8, 0),'y': (np.int8, 1)})))
# (numpy.int16, [('x', 'i1'), ('y', 'i1')])
print(np.dtype({'names': ['gender', 'age'], "formats": ['S1', np.uint8]}))
# [('gender', 'S1'), ('age', 'u1')]
print(np.dtype({'surname': ('S25', 0), 'age': ('uint8', 25)}))
# [('surname', 'S25'), ('age', 'u1')]