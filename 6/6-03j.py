import numpy as np
import matplotlib.pyplot as plt
#==================パラメータ======================
m = 1.0
M = 1.0
G = 1.0
g = 9.80
dt = 0.010
step = 400
#==================初期条件======================
plt.scatter(0,0,s=20,c="red")
x = 1.0
y = 0.0
vx = 0.0
vy = 0.50
t = 0.0
plt.scatter(x,y,s=5,c="blue")
#==================シンプレクティック法======================
for n in range(0,step+1):
    t = float(n) * dt
    r = np.sqrt(x**2+y**2)
    f = - G * M * m / (r**2)
    vx = vx + dt * f * x / (m*r)
    vy = vy + dt * f * y / (m*r)
    x = x + vx * dt
    y = y + vy * dt
    plt.scatter(x,y,s=5,c="blue")
plt.show()