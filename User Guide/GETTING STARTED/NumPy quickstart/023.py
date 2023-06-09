import numpy as np
a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
print(a)
b = a
print(b)
print(b is a)

print(id(a))
def f(x):
    print(id(x))


print(f(a))