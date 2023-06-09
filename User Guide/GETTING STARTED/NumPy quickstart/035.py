import numpy as np
a = np.array([2, 3, 4, 5])
print(a)
b = np.array([8, 5, 4])
print(b)
c = np.array([5, 4, 6, 8, 3])
print(c)
ax, bx, cx = np.ix_(a, b, c)
print(ax)
print(ax.shape)
print(bx)
print(bx.shape)
print(cx)
print(cx.shape)
print(ax + bx + cx)
result = ax + bx * cx
print(result)
print(result[3, 2, 4])
print(a[3] + b[2] * c[4])