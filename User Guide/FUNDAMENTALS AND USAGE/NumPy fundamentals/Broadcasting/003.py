import numpy as np
"""
For example, if you have a 256x256x3 array of RGB values, 
and you want to scale each color in the image by a different value, 
you can multiply the image by a one-dimensional array with 3 values. 
"""
image = np.random.Generator.random(size=(256,256,3))
scale = np.random.Generator.random(size=(3,))
print(image * scale)

