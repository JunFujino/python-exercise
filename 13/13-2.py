import numpy as np
import matplotlib.pyplot as plt
N = 100
y = np.empty(N+1)
for i in range(N+1):
    y[i] = np.sin(2*np.pi*i/N)
    plt.plot(y,'bo')
plt.show()