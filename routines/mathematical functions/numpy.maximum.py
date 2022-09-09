"""
numpy.maximum(
                x1,
                x2,
                /,
                out=None,
                *,
                where=True,
                casting='same_kind',
                order='K',
                dtype=None,
                subok=True[, signature, extobj]) = <ufunc 'maximum'>
数组元素的元素间最大值。

比较两个数组并返回一个新的数组，其中包含元素的最大值。
如果被比较的元素之一是NaN，那么该元素被返回。
如果两个元素都是NaN，则返回第一个元素。
后者的区别对于复数NaNs很重要，复数NaNs的定义是至少有一个实部或虚部是NaN。
最终的效果是NaNs被传播了。


"""