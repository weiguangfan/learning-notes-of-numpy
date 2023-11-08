import numpy as np


def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
print(b)
for row in b:
    print(row)
    
for element in b.flat:
    print(element)