import matplotlib.pyplot as plt
#==============初期条件===============
v = 0.0
t = 0.0
#==============パラメータ===============
g = 9.80
dt = 0.10
B = 1.0
m = 1.0
nstep = 400
plt.scatter(t,v,s=5,c="blue")
for n in range(1,nstep+1):
    v = v + ( g - B * v / m ) * dt
    t = t + dt
    plt.scatter(t,v,s=5,c="blue")
plt.show()
