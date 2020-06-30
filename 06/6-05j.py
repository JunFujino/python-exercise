import numpy as np
import matplotlib.pyplot as plt
color = ["r", "g", "b", "c", "m", "y", "k", "darkblue"]
#==================パラメータ======================
m = 1.0
M = 1.0
G = 1.0
g = 9.80
dt = 0.010
step = 400
itr = 8
plt.scatter(0,0,s=20,c="red")       #恒星の位置
for i in range(0,itr):
    #==================初期条件======================
    x = 1.0
    y = 0.0
    t = 0.0
    vx = 0.0
    vy = 0.50 + float(i) * 0.10
    plt.scatter(x,y,s=5,c=color[i])
    #==================時間発展======================
    for n in range(0,step+1):
        t = float(n) * dt
        r = np.sqrt(x**2+y**2)
        f = - G * M * m / (r**2)
        vx = vx + dt * f * x / (m*r)
        vy = vy + dt * f * y / (m*r)
        x = x + vx * dt
        y = y + vy * dt
        plt.scatter(x,y,s=5,c=color[i])
plt.show()