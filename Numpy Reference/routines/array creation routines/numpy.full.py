"""
numpy.full(
            shape,
            fill_value,
            dtype=None,
            order='C',
            *,
            like=None)
返回一个给定形状和类型的新数组，用fill_value填充。

Parameters
    shape: int or sequence of ints
        新数组的形状，例如，(2, 3)或2。

    fill_value: scalar or array_like
                填充值。

    dtype：data-type, optional
        数组所需的数据类型 默认情况下，无，意味着
        np.array(fill_value).dtype.

    order: {‘C’, ‘F’}, optional
        是否在内存中以C-或Fortran-连续（行或列）的顺序存储多维数据。

    like: array_like, optional
        参考对象，允许创建非NumPy数组的数组。
        如果作为like传入的数组支持__array_function__协议，其结果将由其定义。
        在这种情况下，它确保创建的数组对象与通过该参数传入的数组对象兼容。

        在1.20.0版本中新增。

Returns
    out: ndarray
        具有给定形状、dtype和顺序的fill_value的数组。

"""
import numpy as np

print(np.full((2, 2), np.inf))
print(np.full((2, 2), 10))
print(np.full((2, 2), [1, 2]))
