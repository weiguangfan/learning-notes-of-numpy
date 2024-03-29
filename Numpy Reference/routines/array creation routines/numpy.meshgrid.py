"""
numpy.meshgrid(
                *xi,
                copy=True,
                sparse=False,
                indexing='xy')

从坐标向量返回坐标矩阵。

制作N-D坐标阵列，用于在N-D网格上对N-D标量/矢量场进行矢量化评估，给定一维坐标阵列x1, x2,..., xn。

meshgrid对于评估网格上的函数非常有用。
如果函数依赖于所有坐标，你可以使用参数sparse=True来节省内存和计算时间。


Parameters:
x1, x2,..., x : narray_like
            代表网格坐标的一维数组。

indexing : {'xy', 'ij'}, 可选
        输出的笛卡尔（'xy'，默认）或矩阵（'ij'）索引。更多细节见注释。

        在1.7.0版本中新增。

sparse : bool, optional
        如果为True，返回的坐标阵列的维度i的形状将从（N1, ..., Ni, ... Nn）减少到（1, ..., 1, Ni, 1, ..., 1）。
        这些稀疏的坐标网格是为了与广播（Broadcasting）一起使用。
        当一个表达式中使用了所有的坐标时，广播仍然会导致一个全单调的结果数组。

        默认为False。

        在1.7.0版本中新增。

copy : bool, optional
        如果是假的，则返回原始数组的视图，以节省内存。
        默认为True。
        请注意，sparse=False，copy=False将可能返回非连续的数组。
        此外，一个广播数组中的多个元素可能会指代一个内存位置。
        如果你需要对数组进行写入，请先进行复制。

        在1.7.0版本中新增。

Returns
    X1, X2,..., XN : ndarray
    对于长度为Ni=len(xi)的向量x1, x2,..., xn，
    如果索引='ij'，则返回(N1, N2, N3,..., Nn)形状的数组，
    如果索引='xy'，则返回(N2, N1, N3,..., Nn)形状的数组，
    对于x1，第二维，以此类推，xi的元素会沿第一维重复填充矩阵。

"""
import numpy as np
import matplotlib.pyplot as plt
# nx,ny = (3,2)
# x = np.linspace(0,1,nx)
# print(x)
# y = np.linspace(0,1,ny)
# print(y)
# xv,yv = np.meshgrid(x,y)
# print(xv)
# print(yv)
#
# xv,yv = np.meshgrid(x,y,sparse=True)
# print(xv)
# print(yv)

x = np.linspace(-5,5,101)
print(x.shape)
y = np.linspace(-5,5,101)
print(x.size)
xx,yy = np.meshgrid(x,y)
print(xx.shape)
print(yy.shape)

zz = np.sqrt(xx**2 + yy**2)
print(zz.shape)

xs,ys = np.meshgrid(x,y,sparse=True)
zs = np.sqrt(xs**2 + ys**2)
print(xs.shape)
print(ys.shape)
print(zs.shape)
print(np.array_equal(zz, zs))

h = plt.contourf(x,y,zs)
plt.axis('scaled')
plt.colorbar()
plt.show()