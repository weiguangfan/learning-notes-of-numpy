import numpy as np
a = np.arange(10)**3
print(a)
print(a[2])
print(a[2:5])
a[:6:2] = 1000
print(a)
print(a[::-1])
for i in a:
    print(i**(1 / 3.))