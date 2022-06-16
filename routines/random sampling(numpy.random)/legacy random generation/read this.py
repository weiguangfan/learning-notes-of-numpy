"""
RandomState提供了对传统生成器的访问。
这个发生器被认为是冻结的，不会有进一步的改进。
它保证产生与NumPy v1.16的最终点版本相同的值。
这些都取决于Box-Muller法线或反CDF指数或gammas。
只有在必须要有与NumPy以前版本产生的相同的随机数时，才可以使用这个类。

RandomState为状态添加了额外的信息，
这在使用Box-Muller法线时是需要的，因为这些是成对产生的。
重要的是，在访问状态时要使用RandomState.get_state，而不是底层的比特生成器状态，这样才能保存这些额外的值。

虽然我们提供了MT19937 BitGenerator用于独立于RandomState的使用，
但请注意，它的默认播种使用SeedSequence而不是传统的播种算法。
RandomState将使用传统的播种算法。
使用传统播种算法的方法目前是私有的，因为使用它们的主要原因只是为了实现RandomState。
然而，人们可以使用RandomState的状态来重置MT19937的状态。

class numpy.random.RandomState(seed=None):
缓慢的Mersenne Twister伪随机数发生器的容器。
可以考虑用一个不同的BitGenerator来代替Generator容器。
RandomState和Generator暴露了一些用于生成从各种概率分布中抽取的随机数的方法。
除了特定的分布参数外，每个方法都需要一个默认为None的关键字参数size。
如果size是None，那么就会生成并返回一个单一的值。
如果size是一个整数，那么就会返回一个充满生成值的一维数组。
如果size是一个元组，那么就填充并返回一个具有该形状的数组。

兼容性保证
    一个使用固定seed的固定bitgenerator和一系列固定的使用相同参数的'RandomState'方法的调用将总是产生相同的结果，
    直到四舍五入的错误，除非值不正确。
    RandomState被有效地冻结了，只接收Numpy内部变化所需的更新。
    更多的实质性变化，包括算法的改进，将保留给generator。

Parameters:
seed:{None, int, array_like, BitGenerator}, optional
    用于初始化伪随机数发生器或实例化的BitGenerator的随机seed。

    如果是一个整数或数组，作为MT19937 BitGenerator的种子使用。
    值可以是0到2**32-1之间的任何整数，也可以是这种整数的数组（或其他序列），或者无（默认）。

    如果种子为None，那么MT19937 BitGenerator将通过从/dev/urandom（或Windows的类似物）读取数据（如果有的话）来初始化，
    否则就从时钟中读取种子。

method
random.RandomState.randn(d0, d1, ..., dn):
返回 "标准正态 "分布的一个（或多个）样本。

note1:
    这是一个方便用户从Matlab移植代码的函数，它封装了standard_normal。
    该函数需要一个元组来指定输出的大小，这与其他NumPy函数如numpy.zeros和numpy. ones一致。
note2:
    新的代码应该使用default_rng()实例的standard_normal方法来代替；请看快速入门。

如果提供了正的int_like参数，randn会生成一个形状为(d0, d1, ..., dn)的数组，
其中充满了从均值为0、方差为1的单变量 "正态"（高斯）分布中抽取的随机浮点数。

如果没有提供参数，则返回一个从分布中随机抽取的单个浮点数。

Parameters:
d0, d1, …, dn:int, optional
    返回数组的尺寸，必须为非负数。
    如果没有给出参数，则返回单个Python float。

Returns:
Z:ndarray or float
    一个(d0, d1, ..., dn)形的标准正态分布的浮点样本数组，
    如果没有提供参数，则是一个单一的此类浮点。
notes:
    对于来自 N(mu, delta**2)的随机样本，使用:
    sigma * np.random.randn(...) + mu
"""
from numpy.random import MT19937
from numpy.random import RandomState
rs = RandomState(12345)
print(rs)
mt19937 = MT19937()
print(mt19937)
print(mt19937.state)
print(rs.get_state())
mt19937.state = rs.get_state()
print(mt19937.state)
rs2 = RandomState(mt19937)
print(rs2)
rs.standard_normal()
rs2.standard_normal()
rs.random()
rs2.random()
rs.standard_exponential()
rs2.standard_exponential()

import numpy as np
a = np.random.randn()
print(a)

b = np.random.randn(2, 4)
print(b)
print(b.size)
print(b.shape)
print(b.ndim)
c = 3 + 2.5 * b
print(c)
