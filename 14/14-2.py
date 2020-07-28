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
#====================================
#   パラメータと初期条件
#====================================
dt = 0.1
x = np.empty(N)
v = np.empty(N)
X = np.empty(N)
Y = np.empty(N)

r = np.random.rand(N)
for n in range(Nt+1):
    v = v + A * (V - v) * dt
    x = x + v * dt

    if(x>=L):
        x = x - L
    theta = 2*np.pi*x/L
    X = np.cos(theta)
    Y = np.sin(theta)
    
    im = plt.plot(X,Y,'ob')     #アニメーション用
    ims.append(im)              #アニメーション用

ani = animation.ArtistAnimation(fig, ims, interval = 10)        #アニメーション用
plt.show()