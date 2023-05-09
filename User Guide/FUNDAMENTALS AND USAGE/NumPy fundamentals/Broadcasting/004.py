import numpy as np
a = np.random.Generator.random(size=(8,1,6,1))
b = np.random.Generator.random(size=(7,1,5))
print(a * b)

