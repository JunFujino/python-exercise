import matplotlib.pyplot as plt
#===========初期条件===========
t = 0.0
v = 0.0
x = 1.0
#==========パラメータ===========
#g = 9.80
k = 1.0
m = 1.0
dt = 0.10
nstep = 400
plt.scatter(x,t,s=5,c="blue")
#==========シンプレクティック法===========
for n in range(1,nstep+1):
    v = v - k * x * dt / m
    x = x + v * dt
    t = t + dt
    plt.scatter(t,x,s=5,c="blue")
plt.show()
