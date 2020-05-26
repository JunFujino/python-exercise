import matplotlib.pyplot as plt
v = 0.0     #初期条件
t = 0.0
g = 9.80
dt = 0.10
nstep = 400
plt.scatter(v,t,s=5,c="blue")
for n in range(1,nstep+1):
    v = v + g * dt
    t = t + dt
    plt.scatter(t,v,s=5,c="blue")
plt.show()
