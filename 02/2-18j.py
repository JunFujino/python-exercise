import numpy as np
a=np.array([1,1,1])
b=np.array([2,1,1])
c=np.cross(a,b)
print("c =",c)
print("内積",np.dot(a,c))
