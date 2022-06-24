"""
class numpy.nditer(
                    op,
                    flags=None,
                    op_flags=None,
                    op_dtypes=None,
                    order='K',
                    casting='safe',
                    op_axes=None,
                    itershape=None,
                    buffersize=0)
Parameters:
op:ndarray or sequence of array_like
    要迭代的数组。
flags: sequence of str, optional
    用于控制iterator行为的标志。
    buffered 在需要时启用缓冲功能。
    c_index  导致追踪一个C-order索引。
    f_index 使一个Fortran顺序的索引被追踪。
    multi_index 导致跟踪一个多索引，或者一个每个迭代维度有一个索引的元组。
    common_dtype 导致所有的操作数被转换为一个共同的数据类型，并在必要时进行复制或缓冲。
    copy_if_overlap 使迭代器确定读操作数是否与写操作数重叠，并在必要时进行临时拷贝以避免重叠。
        在某些情况下可能会出现假阳性（不必要的复制）。
    delay_bufalloc  延迟分配缓冲区，直到调用reset()。
        允许分配的操作数在其值被复制到缓冲区之前被初始化。
    external_loop 使给出的值成为具有多个值的一维数组，而不是零维数组。
    grow_inner 允许当缓冲区和external_loop都被使用时，使值数组的大小大于缓冲区的大小。
    ranged 允许将迭代器限制在iterindex值的一个子范围内。
    refs_ok 允许对引用类型进行迭代，例如对象数组。
    reduce_ok 允许对被广播的读写操作数进行迭代，也被称为减少操作数。
    zerosize_ok 允许itersize为零。
op_flags:list of list of str, optional
    这是每一个操作数的标志的列表。至少必须指定readonly, readwrite, 或writeonly中的一个。
    readonly表示该操作数将只被读出。
    readwrite表示该操作数将被读出和写入。
    writeonly表示操作数只能被写入。
    no_broadcast防止操作数被广播。
    contig强制操作数为连续的。
    aligned强制要求操作数是对齐的。
    nbo强制操作数以本地字节为序。
    copy允许在需要时进行临时的只读拷贝。
    updateifcopy允许在需要时进行临时的读写拷贝。
    allocate如果在op参数中为None，则导致数组被分配。
    no_subtype防止allocate操作数使用一个子类型。
    arraymask表示这个操作数是在写给设置了'writemasked'标志的操作数时用来选择元素的掩码。
        迭代器并不强制执行，但是当从缓冲区写回数组时，它只复制这个掩码所指示的那些元素。
    writemasked表示只有选择arraymask操作数为True的元素会被写入。
    overlap_assume_elementwise可以用来标记只按迭代器顺序访问的操作数，以便在copy_if_overlap出现时允许更保守的复制。



"""




