import numpy as np
"""
class numpy.dtype(type, align=False, copy=False)
创建一个数据类型对象。

numpy数组是同质的，它包含由dtype对象描述的元素。一个dtype对象可以由基本数字类型的不同组合构成。
"""
# Using array-scalar type:
print(np.dtype(np.int16))
# int16
print(type(np.dtype(np.int16)))
# <class 'numpy.dtype[int16]'>

# Structured type, one field name ‘f1’, containing int16:
print(np.dtype([('f1', np.int16)]))
# [('f1', '<i2')]

# Structured type, one field named ‘f1’, in itself containing a structured type with one field:
print(np.dtype([('f1', [('f1', np.int16)])]))
# [('f1', [('f1', '<i2')])]

# Structured type, two fields: the first field contains an unsigned int, the second an int32:
print(np.dtype([('f1', np.uint64), ('f2', np.int32)]))
# [('f1', '<u8'), ('f2', '<i4')]

# Using array-protocol type strings:
print(np.dtype([('a', 'f8'), ('b', 'S10')]))
# [('a', '<f8'), ('b', 'S10')]

# Using comma-separated field formats. The shape is (2,3):
print(np.dtype('i4,(2,3)f8'))
# [('f0', '<i4'), ('f1', '<f8', (2, 3))]

# Using tuples. int is a fixed type, 3 the field’s shape. void is a flexible type, here of size 10:
print(np.dtype([("hello", (np.int64, 3)), ('world', np.void, 10)]))
# [('hello', '<i8', (3,)), ('world', 'V10')]

# Subdivide int16 into 2 int8’s, called x and y. 0 and 1 are the offsets in bytes:
print(np.dtype((np.int16, {'x': (np.int8, 0),'y': (np.int8, 1)})))
# (numpy.int16, [('x', 'i1'), ('y', 'i1')])

# Offsets in bytes, here 0 and 25:
print(np.dtype({'surname': ('S25', 0), 'age': ('uint8', 25)}))
# [('surname', 'S25'), ('age', 'u1')]

# Using dictionaries. Two fields named ‘gender’ and ‘age’:
print(np.dtype({'names': ['gender', 'age'], "formats": ['S1', np.uint8]}))
# [('gender', 'S1'), ('age', 'u1')]