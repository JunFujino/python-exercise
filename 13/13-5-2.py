import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure() #アニメーションを出力するウィンドウを生成

ims = [] #画像のリストを作成

N = 100
dt = 0.1
m = 1.0
k = 1.0

Nt = 1000
v = np.empty(N+1)
y = np.empty(N+1)
#初期条件
for i in range(N+1):
    v[i] = 0.0
    y[i] = np.random.rand()
#時間発展（シンプレクティック法）
for nt in range(Nt+1):
    for i in range(1,N):
        v[i] = v[i] + k * (y[i-1] - 2*y[i] + y[i+1]) * dt / m
    for i in range(1,N):
        y[i] = y[i] + v[i]*dt

    if(nt % 10 == 0):
        im = plt.plot(y,'ob') #imとして画像を定義。’ob’は円形の点(o)を青色(b)で書く指定。
        ims.append(im) #imsにimで定義した画像をリストの要素として保存
ani = animation.ArtistAnimation(fig, ims, interval=100)
#出力のウィンドウ(fig)、出力する画像のリスト(ims)、出力の間隔(100ms=0.1s)を指定。
plt.show()