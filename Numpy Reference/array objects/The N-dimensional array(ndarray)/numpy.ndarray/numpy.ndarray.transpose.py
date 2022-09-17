"""
ndarray.transpose(*axes)
返回一个转轴的数组视图。

对于一个一维数组来说，这没有什么影响，因为转置后的向量只是同一个向量。
为了将一个一维数组转换为二维列向量，必须增加一个额外的维度。
np.atleast2d(a).T实现了这一点，a[:, np.newaxis]也是如此。
对于一个二维数组来说，这就是一个标准的矩阵转置。
对于一个n-D数组，如果给出了轴，它们的顺序表明轴是如何被置换的（见示例）。
If axes are not provided and a.shape = (i[0], i[1], ... i[n-2], i[n-1]),
then a.transpose().shape = (i[n-1], i[n-2], ... i[1], i[0]).

Parameters
    axes: None, tuple of ints, or n ints

        None or no argument: 颠倒轴的顺序。

        tuple of ints：i在tuple的第j个位置意味着a的第i个轴变成a.transpose()的第j个轴。

        n ints：与相同ints的n个元组相同（这种形式只是作为元组形式的一个 "方便 "的替代品）


Returns
    out: ndarray
        a的视图，并对轴进行适当的变换。

"""