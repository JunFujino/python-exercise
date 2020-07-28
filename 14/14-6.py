import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#====================================
#   パラメータ
#====================================
Nt = 1000
L = 30
V = 1.0
A = 1.0
B = 1.0
C = 2.0
tmp = np.empty(39)
Ntmp = np.empty(39)
#====================================
#   パラメータと初期条件
#====================================
dt = 0.1
for N in range(2,41):
    tmp[N-2] = 0
    x = np.empty(N)
    v = np.empty(N)
    X = np.empty(N)
    Y = np.empty(N)
    r = np.random.rand(N)
    for i in range(N):
        x[i] = (i+r[i])*L/N
        v[i] = 0
    for n in range(Nt+1):
        for i in range(N):
            if(i<N-1):
                dx = x[i+1] - x[i]
            else:
                dx = x[0] - x[N-1]
            if(dx<0):
                dx = dx + L 
            V = np.tanh(dx-C) + np.tanh(C)
            v[i] =  v[i] + A * (V - v[i]) * dt
        for i in range(N):
            x[i] = x[i] + v[i] * dt
            if(x[i]>=L):
                x[i] = x[i] - L
                tmp[N-2] = tmp[N-2] + 1
    Ntmp[N-2] = N
plt.plot(Ntmp,tmp,'b-') 
plt.show()