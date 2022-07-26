"""
method

ndarray.tolist()
将数组作为Python标量的a.ndim-levels深度嵌套列表返回。

将数组数据的副本作为一个 (嵌套的) Python 列表返回。
数据项通过 item 函数被转换为最接近的兼容的 Python 内置类型。

如果a.ndim为0，那么由于嵌套列表的深度为0，它将根本不是一个列表，而是一个简单的Python标量。

Parameters
    无
Returns
    y: object, or list of object, or list of list of object, or …
    可能是嵌套的数组元素的列表。

数组可以通过a = np.array(a.tolist())重新创建，尽管这样做有时会失去精度。
"""
import numpy as np
# 对于一个一维数组，a.tolist()与list(a)几乎相同，只是tolist将numpy标量改为Python标量。
# a = np.uint32([1,2])
# print(a)
# a_list = list(a)
# print(a_list)
# print(type(a_list[0]))
# a_tolist = a.tolist()
# print(a_tolist)
# print(type(a_tolist[0]))

# 此外，对于一个二维数组，tolist是递归适用的。
# b = np.array([[1,2],[3,4]])
# print(b)
# print(list(b))
# print(b.tolist())

# 这个递归的基本情况是一个0D阵列。
c = np.array(1)
print(c)
# print(list(c))
print(c.tolist())

