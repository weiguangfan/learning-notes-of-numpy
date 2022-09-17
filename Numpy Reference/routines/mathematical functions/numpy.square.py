"""
numpy.square(
                x,
                /,
                out=None,
                *,
                where=True,
                casting='same_kind',
                order='K',
                dtype=None,
                subok=True[, signature, extobj]
                ) = <ufunc 'square'>
返回输入元素的平方。


Parameters:
x：array_like
    输入数据。
out：ndarray,None, or tupel of ndarray and None, optinal
    一个储存结果的位置。
    如果提供，它必须有一个输入广播的形状。
    如果没有提供或没有，将返回一个新分配的数组。
    一个元组（只可能作为关键字参数）的长度必须等于输出的数量。

where：array_like, optional
    这个条件在输入中被广播。
    在条件为True的地方，输出数组将被设置为ufunc的结果。
    在其他地方，输出数组将保留其原始值。
    注意，如果通过默认的out=None创建了一个未初始化的out数组，其中条件为False的位置将保持未初始化。

**kwargs
关于其他只用关键字的参数，见ufunc文档。

"""
import numpy as np

print(np.square([-1j, 1]))

