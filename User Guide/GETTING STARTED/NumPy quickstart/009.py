import numpy as np
# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# print(a)
# print(b)
# c = a - b
# print(c)
# d = b ** 2
# print(d)
# e = 10 * np.sin(a)
# print(e)
# f = a < 35
# print(f)
# myOnes = np.ones([3,3])
# print(myOnes)
# myEye = np.eye(3)
# print(myEye)
# print(myOnes + myEye)
# print(myOnes - myEye)
myMatrix = np.mat([[1,2,3],[4,5,6],[7,8,9]])
print(myMatrix)

# myMatrix2 = np.mat([[1],[2],[3]])
# print(myMatrix2)

# print(myMatrix[0])
# print(myMatrix.T[0])

myCopyMatrix = myMatrix.copy()
print(myCopyMatrix)


# print(np.matmul(myMatrix, myMatrix2))
# print(myMatrix * myMatrix2)

# print(myMatrix.T)
# print(myMatrix.transpose())

# a = 10
# print(a * myMatrix)
# print(myMatrix.sum())
# b = np.ones([3,3])
# print(b)
# print(1.5 * b)

# print(np.multiply(b, myMatrix))

# print(np.power(myMatrix, 2))