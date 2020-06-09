import numpy as np
import matplotlib.pyplot  as plt
import random
N = 1000
x = np.zeros(N+1)
x[0] = 0.0
dx = 1.0
for i in range(0,N):
    a = random.random()
    if a>0.50:
        x[i+1] = x[i] + dx
    else:
        x[i+1] = x[i] - dx
plt.plot(x,'-o')
plt.show()