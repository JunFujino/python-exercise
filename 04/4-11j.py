import matplotlib.pyplot as plt
import numpy as np
x=np.empty(100)
y=np.empty(100)
for i in range(100):
  x[i]=0.1*i
  y[i]=np.sin(x[i])
plt.plot(x,y)
plt.show()
