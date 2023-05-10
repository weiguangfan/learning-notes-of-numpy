import numpy as np
dt = np.dtype([('name',np.unicode_,16),('grades',np.float64,(2,),)])
print(dt)
# [('name', '<U16'), ('grades', '<f8', (2,))]
print(dt['name'])
# <U16
print(dt['grades'])
# ('<f8', (2,))

x = np.array([('Sarah',(8.0,7.0)),('John',(6.0,7.0))],dtype=dt)
print(x)
# [('Sarah', [8., 7.]) ('John', [6., 7.])]
print(x[1])
# ('John', [6., 7.])
print(x[1]['grades'])
# [6. 7.]
print(type(x[1]))
# <class 'numpy.void'>
print(type(x[1]['grades']))
# <class 'numpy.ndarray'>