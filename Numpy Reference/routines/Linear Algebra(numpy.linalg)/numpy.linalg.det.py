import numpy as np
myMatrix = np.mat([[1,2,4,5,7,],[9,12,11,8,2,],[6,4,3,2,1,],[9,1,3,4,5],[0,2,3,4,1]])
print(myMatrix)
print(myMatrix.shape)
print(np.linalg.det(myMatrix))