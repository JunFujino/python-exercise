import numpy as np
import matplotlib.pyplot  as plt
mu = 4.0
N = 100  
x = np.zeros(N+1)
y = np.zeros(N+1)
delta = np.zeros(N+1)
delta[0] = pow(10,-10)
x[0] = 0.19  
y[0] = x[0] + delta[0]
for i in range(0,N):
    x[i+1] = mu * x[i] * (1.0 -x[i])
    y[i+1] = mu * y[i] * (1.0 -y[i])
    delta[i+1] = np.abs(y[i+1]-x[i+1])
#plt.plot(x,'-o')
#plt.plot(y,'-o')
plt.xlabel("n")
plt.ylabel("delta")
#plt.plot(delta, '-o')
plt.plot(np.log(delta), '-o')
plt.show()