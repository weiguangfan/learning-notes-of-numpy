"""
numpy.arange(
            [start,
            ]stop,
            [step,
             ]dtype=None,
             *,
             like=None)
在一个给定的区间内返回均匀的数值。

arange可以用不同数量的位置参数被调用。

arange(stop): 在半开区间[0, stop)内生成数值（换句话说，包括开始但不包括停止的区间）。

arange(start, stop): 在半开放区间[start, stop)内生成数值。

arange(start, stop, step) 在半开放区间[start, stop)内生成数值，数值之间的间隔由步骤决定。

对于整数参数，该函数大致相当于Python内置的range，但返回一个ndarray而不是一个range实例。

当使用非整数步长时，例如0.1，通常使用numpy.linspace更好。

更多信息见下面的警告部分。

Parameters
    start：integer or real, optional
            区间的起点。
            区间包括这个值。
            默认的开始值是0。

    stop： integer or real
            间隔期的结束。
            区间不包括这个值，
            除非在某些情况下，
            步长不是整数，
            浮点四舍五入会影响out的长度。

    step：integer or real, optional
            值之间的间距。
            对于任何输出的out，
            这是两个相邻值之间的距离，out[i+1] - out[i]。
            默认步长为1。
            如果step被指定为一个位置参数，
            则必须同时给出start。

    dtype: dtype, optional
            输出数组的类型。
            如果没有给出dtype，
            从其他输入参数中推断出数据类型。

    like: array_like, optional
            参考对象，
            允许创建非NumPy数组的数组。
            如果作为like传入的数组支持__array_function__协议，
            其结果将由其定义。
            在这种情况下，
            它确保创建的数组对象与通过该参数传入的数组对象兼容。
Returns
    arange: ndarray
        均匀间隔的数值的数组。
        对于浮点参数，结果的长度是ceil((stop - start)/step)。
        由于浮点溢出，这个规则可能导致out的最后一个元素大于stop。

输出的长度可能在数值上不稳定。

另一个稳定性问题是由于numpy.range的内部实现。
用于填充数组的实际步骤值是dtype(start + step) - dtype(start)，
而不是step。
由于铸造或在start远大于step时使用浮点，
这里可能发生精度损失。
这可能会导致意外的行为。比如说:


"""
import numpy as np
a = np.arange(0,5,0.5,dtype=int)
# a = np.linspace(0,5,num=11)
print(a)

b = np.arange(-3,3,0.5,dtype=int)
# b = np.linspace(-3,3,num=13)
print(b)
# 在这种情况下，应该首选使用numpy.linspace。
"""
内置的range产生具有任意大小的Python内置整数，
而numpy.range产生numpy.int32或numpy.int64数字。
这可能导致大整数值的不正确结果。
"""
power = 40
modulo = 10000
x1 = [(n ** power) % modulo for n in range(8)]
print(x1)
x2 = [(n ** power) % modulo for n in np.arange(8)]
print(x2)

a1 = np.arange(3)
print(a1)

b1 = np.arange(3.)
print(b1)

c1 = np.arange(3,7)
print(c1)

d1 = np.arange(3,7,2)
print(d1)
