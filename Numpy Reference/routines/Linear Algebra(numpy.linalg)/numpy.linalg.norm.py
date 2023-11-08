import numpy as np
A = [8,1,6]
print(type(A))
print(A)
print(np.power(A, 2))
print(sum(np.power(A, 2)))
modA = np.sqrt(sum(np.power(A,2)))
print(modA)
# L2范数
normA = np.linalg.norm(A)
print(type(normA))
print(normA)