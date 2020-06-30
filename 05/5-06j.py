import matplotlib.pyplot as plt
#==========パラメータ===========
#g = 9.80
k = 1.0
m = 1.0
dt = 0.10
nstep = 400
itr = 15
B = 0.0
for i in range(0,itr+1):
    #===========初期条件===========
    B = 0.200 * float(i)
    t = 0.0
    v = 0.0
    x = 1.0
    #==========シンプレクティック法===========
    for n in range(1,nstep+1):
        v = v - k * x * dt / m -  B * v * dt / m
        x = x + v * dt
        t = t + dt
        if x<0:
            print("振動する B =",B)
            break
    if n==400:
        print("振動しない B =",B)
            