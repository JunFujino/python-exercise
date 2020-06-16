import matplotlib.pyplot  as plt
mu0 = 1.50
K = 101
dmu = 0.0250
N=50
m=20
for i in range(0,K):
    mu = mu0 + i * dmu
    print('mu =',mu)
    x = 0.10
    for j in range(N+m):
        x = mu * x * (1.0 - x)
        if j >= N:
            plt.scatter(j,x,c='blue' )
plt.show()