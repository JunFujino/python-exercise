import matplotlib.pyplot as plt
#初期条件
v = 0.0
t = 0.0
#パラメータ
g = 9.80
dt = 0.10
nstep = 400
#点を表示していく
plt.scatter(v,t,s=5,c="blue")
for n in range(1,nstep+1):
    v = v + g * dt
    t = t + dt
    plt.scatter(t,v,s=5,c="blue")
plt.show()
