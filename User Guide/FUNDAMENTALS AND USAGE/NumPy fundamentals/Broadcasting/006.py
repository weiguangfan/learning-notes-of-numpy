"""
An example of broadcasting when a 1-d array is added to a 2-d array
"""
import numpy as np
a = np.array([[0.0,0.0,0.0],
              [10.0,10.0,10.0],
              [20.0,20.0,20.0],
              [30.0,30.0,30.0]
              ])
b = np.array([1.0,2.0,3.0])
print(a + b)





