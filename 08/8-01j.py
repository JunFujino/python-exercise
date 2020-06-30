import matplotlib.pyplot as plt
mu0 = 1.50
K = 100
dmu = 0.0250
N=50  
m=20    #各muに対してうつ点の数
for i in range(0,K+1):
    mu = mu0 + i * dmu
    print('mu =',mu)
    x = 0.10
    #================時間発展======================
    for j in range(N+m):
        x = mu * x * (1.0 - x)
        if j >= N:      # N（時間）たったら振る舞いを表示．
            plt.scatter(mu,x,c='blue',s=3)
plt.show()