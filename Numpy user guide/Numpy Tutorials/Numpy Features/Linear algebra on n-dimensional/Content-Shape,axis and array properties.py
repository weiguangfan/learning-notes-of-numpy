"""
请注意，在线性代数中，向量的维数是指数组中的条目数。
在NumPy中，它反而定义了轴的数量。
例如，一维数组是一个矢量，如[1, 2, 3]，二维数组是一个矩阵，以此类推。

首先，让我们检查一下我们数组中数据的形状。
由于这个图像是二维的（图像中的像素形成一个矩形），我们可能期望用一个二维数组来表示它（一个矩阵）。
然而，使用这个NumPy数组的形状属性给了我们一个不同的结果。

"""
from scipy import misc
import matplotlib.pyplot as plt

img = misc.face()
print(type(img))
plt.imshow(img)
plt.show()

print(img.shape)

"""
输出是一个有三个元素的元组，这意味着这是一个三维数组。
事实上，由于这是一张彩色图像，而且我们使用了imread函数来读取它，数据被组织在三个二维数组中，代表颜色通道（在这种情况下，红色、绿色和蓝色 - RGB）。
你可以通过观察上面的形状看到这一点：它表明我们有一个由3个矩阵组成的数组，每个都有768x1024的形状。

此外，使用这个数组的ndim属性，我们可以看到
"""

print(img.ndim)

"""
NumPy将每个维度称为轴。
由于imread的工作原理，第三轴的第一个索引是图像的红色像素数据。
我们可以使用语法来访问它
"""

print(img[:, :, 0])

"""
从上面的输出中，
我们可以看到img[:, :, 0]中的每个值都是0到255之间的整数，
代表每个对应的图像像素中的红色程度
（请记住，如果你使用自己的图像而不是scipy.misc.face，这可能会有所不同）。

正如预期，这是一个768x1024的矩阵。
"""
print(img[:, :, 0].shape)

"""
由于我们要对这些数据进行线性代数运算，因此在矩阵的每个条目中用0和1之间的实数来表示RGB值可能更有意思。
我们可以通过设置
"""
img_array = img/255

"""
由于NumPy的广播规则，这个操作，即用一个数组除以一个标量，是有效的。
(注意，在现实世界的应用中，最好使用例如scikit-image的img_as_float实用函数）。

你可以通过做一些测试来检查上述方法是否有效；例如，查询这个数组的最大值和最小值。

"""

print(img_array.max())
print(img_array.min())

"""
或检查数组中的数据类型：
"""
print(img_array.dtype)

"""
注意，我们可以使用切片语法将每个颜色通道分配给一个单独的矩阵。
"""
red_array = img[:,:,0]
green_array = img[:,:,1]
blue_array = img[:,:,2]

