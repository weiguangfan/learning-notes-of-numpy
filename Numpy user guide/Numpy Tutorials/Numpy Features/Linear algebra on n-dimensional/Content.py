"""
在本教程中，我们将使用线性代数中的矩阵分解，即奇异值分解，来生成一个图像的压缩近似值。
我们将使用scipy.misc模块中的人脸图像。


"""
from scipy import misc
img = misc.face()

"""
注意。
如果你愿意，你可以在学习本教程时使用你自己的图片。
为了将你的图像转换成可以操作的NumPy数组，你可以使用matplotlib.pyplot子模块中的imread函数。
或者，你也可以使用imageio库中的imageio.imread函数。
请注意，如果你使用自己的图像，你可能需要调整下面的步骤。
关于图像转换为NumPy数组时如何处理的更多信息，请参见scikit-image文档中关于图像的NumPy速成课程。

现在，img是一个NumPy数组，我们可以在使用type函数时看到。

"""
print(type(img))
"""
我们可以使用matplotlib.pyplot.imshow函数和特殊的iPython命令--%matplotlib inline来显示内联的图画。
"""
import matplotlib.pyplot as plt
# %matplotlib inline
plt.imshow(img)
plt.show()

