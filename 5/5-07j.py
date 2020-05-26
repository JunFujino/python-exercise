import matplotlib.pyplot as plt
import numpy as np
#==========パラメータ===========
#g = 9.80
k = 1.0
m = 1.0
B = 0.10
E = 1.0
dt = 0.10
nstep = 1000
itr = 10
dw = 0.20
for i in range(0,itr+1):
    #===========初期条件===========
    w = dw * float(i)
    t = 0.0
    v = 0.0
    x = 1.0
    flg = 0
    #==========シンプレクティック法===========
    for n in range(1,nstep+1):
        v = v - k * x * dt / m -  B * v * dt / m + E * dt * np.sin(w*t) / m
        x = x + v * dt
        t = t + dt
        if x>5:
            flg=1
    if flg==1:
        w = dw * float(i)
        t = 0.0
        v = 0.0
        x = 1.0
        plt.scatter(t,x,s=5,c="b")
        for n in range(1,nstep+1):
            v = v - k * x * dt / m -  B * v * dt / m + E * dt * np.sin(w*t) / m
            x = x + v * dt
            t = t + dt
            plt.scatter(t,x,s=5,c="b")
        print(float(i)*dw)
        plt.show()