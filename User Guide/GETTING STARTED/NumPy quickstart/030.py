import numpy as np
time = np.linspace(20, 145, 5)
print(time)
data = np.sin(np.arange(20)).reshape(5, 4)
print(data)
ind = data.argmax(axis=0)
print(ind)
time_max = time[ind]
print(time_max)
data_max = data[ind, range(data.shape[1])]
print(data_max)
print(np.all(data_max == data.max(axis=0)))