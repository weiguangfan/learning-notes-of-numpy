import numpy as np
a = np.array([2, 3, 4, 5])
print(a)
b = np.array([8, 5, 4])
print(b)
c = np.array([5, 4, 6, 8, 3])
print(c)
print(np.add.identity)

def ufunc_reduce(ufct, *vectors):
    vs = np.ix_(*vectors)
    print(vs)
    r = ufct.identity
    print(r)
    for v in vs:
        r = ufct(r, v)
    return r


print(ufunc_reduce(np.add, a, b, c))