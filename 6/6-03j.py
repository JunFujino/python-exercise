import numpy as np
import matplotlib.pyplot as plt
#==================パラメータ======================
m = 1.0
M = 1.0
G = 1.0
g = 9.80
dt = 0.010
itr = 400
#==================初期条件======================
x = 1.0
y = 0.0
vx = 0.0
vy = 0.50
t = 0.0
plt.scatter(x,y,s=5,c="blue")
#==================シンプレクティック法======================
for n in range(0,itr+1):
    t = float(n) * dt
    vy = vy - g * dt
    x = x + vx * dt
    y = y + vy * dt
    plt.scatter(x,y,s=5,c="blue")
plt.show()