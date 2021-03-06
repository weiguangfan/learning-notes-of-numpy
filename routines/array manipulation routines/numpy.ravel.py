"""
numpy.ravel(a, order='C')
返回一个连续的扁平化的数组。

返回一个一维数组，包含输入的元素。
只有在需要的时候才会进行复制。

从NumPy 1.10开始，返回的数组将具有与输入数组相同的类型。
(例如，一个掩码数组的输入将返回一个掩码数组)
Parameters
    a: array_like
        输入数组。
        a中的元素按照order指定的顺序被读取，并打包成一个一维数组。
    order: {‘C’,’F’, ‘A’, ‘K’}, optional
        a的元素使用这个索引顺序被读取。
        C'意味着以行为主，C风格的顺序对元素进行索引，最后一个轴的索引变化最快，回到第一个轴的索引变化最慢。
        F'意味着以列为主，Fortran风格的顺序对元素进行索引，第一个索引变化最快，最后一个索引变化最慢。
        注意，'C'和'F'选项不考虑底层数组的内存布局，只是指轴的索引顺序。
        A'意味着如果a在内存中是Fortran连续的，就按照类似Fortran的索引顺序读取元素，否则就按照C的顺序。
        K "意味着按照元素在内存中出现的顺序来读取它们，除了在stride为负数时将数据反转。
        默认情况下，使用 "C "索引顺序。
Returns
    y: array_like
    y是一个与a具有相同子类型的数组，其形状为（a.size,）。
    注意，为了向后兼容，矩阵是特例，如果a是一个矩阵，那么y就是一个一维的ndarray。
"""