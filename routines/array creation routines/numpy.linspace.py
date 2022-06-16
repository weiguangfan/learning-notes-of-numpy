"""
numpy.linspace(
    start,
    stop,
    num=50,
    endpoint=True,
    retstep=False,
    dtype=None,
    axis=0):
返回指定区间内的均匀间隔的数字。
返回num个均匀间隔的样本，在区间[start, stop]内计算。
区间的端点可以选择性地被排除。

Parameters:
start:array_like
    序列的起始值。
stop:array_like
    序列的结束值，除非endpoint被设置为False。
    在这种情况下，序列由除num + 1的最后一个均匀间隔的样本之外的所有样本组成，因此该stop被排除在外。
    注意，当endpoint为False时，stop会改变。
num:int, optional
    要生成的样本数。
    默认为50。
    必须为非负数。
endpoint:bool, optional
    如果是True，stop是最后一个样本。
    否则，它不包括在内。
    默认为True。
retstep:bool, optional
    如果为True，返回（samples,step），其中step是样本之间的间隔。
dtype:dtype, optional
    输出数组的类型。
    如果没有给dtype，数据类型将从start和stop推断出来。
    推断出的dtype永远不会是一个整数；即使参数会产生一个整数数组，也会选择float。
axis:int, optional
    结果中用于存储样本的轴。
    只有当start或stop是数组形式时才相关。
    默认情况下(0)，样本将沿着在开始时插入的一个新轴。
    使用-1可以在最后得到一个轴。

Returns:
samples:ndarray
    在封闭区间[start,stop]或半开放区间[start,stop)（取决于endpoint是True还是False）有num个等距的样本。
step:float, optional
    只在retstep为True时返回
    采样之间的间距大小。
"""
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(2.0, 3.0, num=5)
print(a)

b = np.linspace(2.0, 3.0, num=5, endpoint=False)
print(b)

c = np.linspace(2.0, 3.0, num=5, retstep=True)
print(c)

N = 8
y = np.zeros(N)
print(y)
x1 = np.linspace(0, 10, N, endpoint=True)
print(x1)
x2 = np.linspace(0, 10, N, endpoint=False)
print(x2)
plt.plot(x1, y, 'o')
plt.plot(x2, y + 0.5, 'o')
plt.ylim([-0.5, 1])
plt.show()

