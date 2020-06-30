import numpy as np
import matplotlib.pyplot as plt
#==================パラメータ======================
m = 1.0
g = 9.80
dt = 0.010
step = 400
#==================初期条件======================
x = 0.0
y = 0.0
vx = 10.0
vy = 10.0
t = 0.0
plt.scatter(x,y,s=5,c="blue")
#==================時間発展======================
for n in range(0,step+1):
    t = float(n) * dt
    vy = vy - g * dt
    x = x + vx * dt
    y = y + vy * dt
    plt.scatter(x,y,s=5,c="blue")
plt.show()