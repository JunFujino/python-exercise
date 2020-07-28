import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt.figure(figsize=(5,5))     #アニメーション用
ims = []                            #アニメーション用
#====================================
#   パラメータ
#====================================
N = 20
Nt = 2000
L = 30
V = 1.0
A = 1.0
B = 1.50
#====================================
#   パラメータと初期条件
#====================================
dt = 0.1
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
        V = B * dx * 0.50
        v[i] =  v[i] + A * (V - v[i]) * dt
    for i in range(N):
        x[i] = x[i] + v[i] * dt
        if(x[i]>=L):
            x[i] = x[i] - L

    for i in range(N):
        theta = 2*np.pi*x[i]/L
        X[i] = np.cos(theta)
        Y[i] = np.sin(theta)
        
    im = plt.plot(X,Y,'ob')     #アニメーション用
    ims.append(im)              #アニメーション用

ani = animation.ArtistAnimation(fig, ims, interval = 10)        #アニメーション用
plt.show()