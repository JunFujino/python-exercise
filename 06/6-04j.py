import numpy as np
import matplotlib.pyplot as plt
color = ["r", "g", "b", "c", "m", "y", "k", "darkblue"]
#==================パラメータ======================
l = 1.0
g = 9.80
dt = 0.10
step = 100
itr = 1
for i in range(0,itr):
    #==================初期条件======================
    theta = 0
    dtheta = 7.0 + float(i) * 0.1 
    t = 0.0
    x = l * np.sin(theta)
    y = - l * np.cos(theta)
    #plt.scatter(t,theta,s=5,c=color[i])
    plt.scatter(x,y,s=5,c=color[i])
    #==================シンプレクティック法======================
    for n in range(0,step+1):
        t = float(n) * dt
        dtheta = dtheta - dt * g * np.sin(theta) / l
        theta = theta + dt * dtheta
        x = l * np.sin(theta)
        y = - l * np.cos(theta)
        #plt.scatter(t,theta,s=5,c=color[i])
        plt.scatter(x,y,s=5,c=color[i])
plt.show()
#dtheta<1くらいの時は，振幅が変わるだけで周期は変わらない！（高校物理！）　
#dthetaが大きくなってくると，周期も変わっていく
#大体，dtheta>6くらいで発散が見れる
#dtheta==7でx,yをプロットしてみる