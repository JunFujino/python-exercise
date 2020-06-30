import numpy as np
import matplotlib.pyplot as plt
#==================パラメータ======================
l = 1.0
g = 9.80
dt = 0.10
step = 100
#==================初期条件======================
theta = 0
dtheta = 0.10
t = 0.0
plt.scatter(t,theta,s=5,c="blue")
#==================シンプレクティック法======================
for n in range(0,step+1):
    t = float(n) * dt
    dtheta = dtheta - dt * g * np.sin(theta) / l
    theta = theta + dt * dtheta
    plt.scatter(t,theta,s=5,c="blue")
plt.show()