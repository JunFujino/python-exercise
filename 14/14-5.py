import numpy as np
import matplotlib.pyplot as plt
#====================================
#   パラメータ
#====================================
N = 20
Nt = 1000
L = 30
V = 1.0
A = 1.0
B = 1.0
C = 2.0
#====================================
#   パラメータと初期条件
#====================================
dt = 0.1
t = np.empty(Nt+1)
xi = np.empty(Nt+1)
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
    xi[n] = x[0]
    t[n] = n * dt
plt.plot(t,xi,'b-') 
plt.show()