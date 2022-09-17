""""
numpy.ceil(
            x,
            /,
            out=None,
            *,
            where=True,
            casting='same_kind',
            order='K',
            dtype=None,
            subok=True[, signature, extobj]
            ) = <ufunc 'ceil'>
返回输入的上限，按元素排列。
标量x的上限是最小的整数i，使i>=x。
它通常被表示为[x]
Parameters
    x: array_like
        输入数据。

    out: ndarray, None, or tuple of ndarray and None, optional
        一个储存结果的位置。
        如果提供，它必须有一个输入广播的形状。
        如果没有提供或None，将返回一个新分配的数组。
        一个元组（只可能作为关键字参数）的长度必须等于输出的数量。

    where: array_like, optional
        这个条件在输入中被广播。
        在条件为True的地方，输出数组将被设置为ufunc的结果。
        在其他地方，输出数组将保留其原始值。
        注意，如果通过默认的out=None创建了一个未初始化的out数组，其中条件为False的位置将保持未初始化。

    **kwargs
        关于其他只用关键字的参数，见ufunc文档。
Returns
    y: ndarray or scalar
        x中每个元素的上限，dtype为float。如果x是一个标量，这就是一个标量。

"""
import numpy as np
a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
print(a)
print(np.ceil(a))  # [-1. -1. -0.  1.  2.  2.  2.]









