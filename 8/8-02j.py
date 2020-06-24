import numpy as np
import matplotlib.pyplot  as plt
#================muを受取り，x[N]からx[N+m]の配列を返す関数==================
def logistic(mu):
    N = 300
    m = 100
    x = np.zeros(N+m+1)
    x[0] = 0.8
    for i in range(N+m):
        x[i+1] = mu * x[i] * (1.0 - x[i])
    return x[N:N+m]
#=============ループ===============================================
for mu in np.linspace(2.4, 4.0, 501):
    x_data = logistic(mu)
    mu_data = np.array([mu]*len(x_data))
    plt.plot(mu_data, x_data, ".", markersize = 1.2,c='blue')
plt.show()