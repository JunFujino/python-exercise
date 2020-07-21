import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt.figure() #アニメーションを出力するウィンドウを生成
ims = [] #画像のリストを作成
N = 100
Nt = 100
x = np.empty(N+1)
y = np.empty(N+1)
for nt in range(Nt+1):
    for i in range(N+1):
        x[i] = np.cos(2*np.pi*(i-nt*0.10)/N)
        y[i] = np.sin(2*np.pi*(i-nt*0.10)/N)
    im = plt.plot(x,y,'ob') #imとして画像を定義。’ob’は円形の点(o)を青色(b)で書く指定。
    ims.append(im) #imsにimで定義した画像をリストの要素として保存
ani = animation.ArtistAnimation(fig, ims, interval=100)
#出力のウィンドウ(fig)、出力する画像のリスト(ims)、出力の間隔(100ms=0.1s)を指定。
plt.show()