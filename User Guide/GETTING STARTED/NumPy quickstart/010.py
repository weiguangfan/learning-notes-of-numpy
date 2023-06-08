import numpy as np
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(A)
print(B)
C = A * B
print(C)
D = A @ B
print(D)
E = A.dot(B)
print(E)