"""
numpy.sin(
            x,
            /,
            out=None,
            *,
            where=True,
            casting='same_kind',
            order='K',
            dtype=None,
            subok=True[, signature, extobj]
            ) = <ufunc 'sin'>
三角正弦，以元素为单位。
Parameters:
    x:array_like
        角度，以弧度为单位（2pi弧度等于360度）。
    out:ndarray, None, or tuple of ndarray and None, optional
        一个储存结果的位置。
        如果提供，它必须有一个输入广播的形状。
        如果没有提供或没有，将返回一个新分配的数组。
        一个元组（只可能作为关键字参数）的长度必须等于输出的数量。
    where:array_like, optional
        这个条件在输入中被广播。
        在条件为True的地方，输出数组将被设置为ufunc的结果。
        在其他地方，out数组将保留其原始值。
        注意，如果通过默认的out=None创建了一个未初始化的out数组，其中条件为False的位置将保持未初始化。
    **kwargs:
        关于其他只用关键字的参数，请参见ufunc文档。

Returns:
y:array_like
    x的每个元素的正弦，如果x是一个标量，这就是一个标量。
Notes:
    正弦是三角学（关于三角形的数学研究）的基本函数之一。
    考虑一个以原点为中心的半径为1的圆。
    一条射线从+x轴进来，在原点形成一个角度（从该轴逆时针测量），然后从原点离开。
    离去的射线与单位圆的交点的y坐标是该角度的正弦。
    其范围从x= 3pi / 2 的-1 到 pi/2 的+1.
    当角度是π的倍数时，该函数有零点。
    在π和2π之间的角的正弦是负的。
    正弦和相关函数的众多属性都包含在任何标准的三角学教材中。

"""
import numpy as np
import matplotlib.pyplot as plt
print(np.sin(np.pi / 2))

print(np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.))

x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.sin(x))
plt.xlabel('angle[rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()

