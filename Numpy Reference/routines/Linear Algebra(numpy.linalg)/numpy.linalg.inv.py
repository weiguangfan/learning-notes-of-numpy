import numpy as np
A = np.mat( [[1,2,4,5,7,],[9,12,11,8,2,],[6,4,3,2,1,],[9,1,3,4,5],[0,2,3,4,1]])
print(A)
print(A.shape)
invA = np.linalg.inv(A)
print(invA)
print(invA.shape)