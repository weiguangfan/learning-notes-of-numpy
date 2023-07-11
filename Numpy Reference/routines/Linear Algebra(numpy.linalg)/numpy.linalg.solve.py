import numpy as np
A = np.mat([[1,2,4,5,7,],[9,12,11,8,2,],[6,4,3,2,1,],[9,1,3,4,5],[0,2,3,4,1]])
print(type(A))
print(A)
print(A.shape)
b = [1,0,1,0,1]
b = np.mat(b)
print(type(b))
print(b)
print(b.shape)
S = np.linalg.solve(A,b.T)
print(type(S))
print(S)
print(S.shape)
