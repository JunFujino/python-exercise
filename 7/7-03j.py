#ブラウン運動のコンピュータ実験
import numpy as np
import matplotlib.pyplot  as plt
import random
#=================パラメータ======================
N = 1000
#=================初期条件========================
x = np.zeros(N+1)
x[0] = 0.0
dx = 1.0
#=================ループ計算======================
for i in range(0,N):
    a = random.random()
    if a>0.50:
        x[i+1] = x[i] + dx
    else:
        x[i+1] = x[i] - dx
#=================図を表示する====================
plt.plot(x,'-o')
plt.show()