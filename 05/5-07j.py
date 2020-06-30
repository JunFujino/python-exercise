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
itr = 20
dw = 0.10
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
        if abs(x)>7.5:   #7.5を超えたら，共振して極大になると判断した．グラフができなければ，ここの値を小さくすればいい
            flg=1
    if flg==1:  #共振したときのグラフのみ表示する
        w = dw * float(i)
        t = 0.0
        v = 0.0
        x = 1.0
        plt.scatter(t,x,s=5,c="b",label="ω =%1.1f" % float(i*dw))
        for n in range(1,nstep+1):
            v = v - k * x * dt / m -  B * v * dt / m + E * dt * np.sin(w*t) / m
            x = x + v * dt
            t = t + dt
            plt.scatter(t,x,s=5,c="b")
        #print(float(i)*dw)
        plt.legend()
        plt.show()
        