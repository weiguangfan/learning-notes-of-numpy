import numpy as np

n1 = np.zeros((2,3))
print(n1.dtype)
# float64

"""
alignment
根据编译器的要求，该数据类型的对齐方式（字节）。
"""
print(n1.dtype.alignment)
# 8

"""
base
返回子数组的基本元素的dtype，无论其尺寸或形状如何。
"""
print(n1.dtype.base)
# float64

"""
byteorder
表示该数据类型对象的字节顺序的一个字符。
"""
print(n1.dtype.byteorder)
# '='

"""
char
21种不同的内置类型中每一种的唯一字符代码。
"""
print(n1.dtype.char)
# 'd'

"""
descr
对数据类型的描述，即__阵列_界面__。
"""
print(n1.dtype.descr)
# [('', '<f8')]

"""
fields
为该数据类型定义的命名字段的字典，或无。
"""
print(n1.dtype.fields)
# None

"""
flags
描述如何解释该数据类型的位标志。
"""
print(n1.dtype.flags)
# 0

"""
hasobject
布尔型，表示该dtype在任何字段或子类型中是否包含任何引用计数的对象。
"""
print(n1.dtype.hasobject)
# False

"""
isalignedstruct
表示dtype是否为保持字段对齐的结构的布尔值。
"""
print(n1.dtype.isalignedstruct)
# False

"""
isbuiltin
整数，表示该dtype与内置dtype的关系。
"""
print(n1.dtype.isbuiltin)
# 1

"""
isnative
布尔值，表示该dtype的字节顺序是否为平台的原生字节。
"""
print(n1.dtype.isnative)
# True

"""
itemsize
这个数据类型对象的元素大小。
"""
print(n1.dtype.itemsize)
# 8

"""
kind
一个字符代码（'biufcmMOSUV'之一），识别数据的一般类型。
"""
print(n1.dtype.kind)
# f

"""
metadata
无或一个只读的元数据字典（mappingproxy）。
"""
print(n1.dtype.metadata)
# None

"""
name
该数据类型的位宽名称。
"""
print(n1.dtype.name)
# float64

"""
names
字段名称的有序列表，如果没有字段，则为无。
"""
print(n1.dtype.names)
# None

"""
ndim
如果该数据类型描述的是一个子数组，那么子数组的维数，否则为0。
"""
print(n1.dtype.ndim)
# 0

"""
num
21种不同的内置类型中每一种的唯一编号。
"""
print(n1.dtype.num)
# 12

"""
shape
如果该数据类型描述了一个子数组，则为该子数组的形状元组，否则为（）。
"""
print(n1.dtype.shape)
# ()

"""
str
这个数据类型对象的数组协议类型字符串。
"""
print(n1.dtype.str)
# <f8

"""
subdtype
如果这个dtype描述的是一个子数组，则为Tuple（item_dtype, shape），否则为None。
"""
print(n1.dtype.subdtype)
# None