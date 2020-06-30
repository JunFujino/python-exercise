import numpy as np
#二次方程式 x**2+b*x+c=0 の解を求めてみる．
b=np.power(10,7)  #係数bの設定
c=-0.250   #係数cの設定
x1=(-b-(np.sqrt(b**2-4*c)))/2.0
x2=(-b+(np.sqrt(b**2-4*c)))/2.0
print("x1 =",x1,"x2 =",x2)
answer1=x1**2+b*x1+c
answer2=x2**2+b*x2+c
print("プラスの方は，桁落ちにより誤差が生まれる，マイナスの方は，有理化したら逆に誤差が生じる．")
print("得られた解を代入した結果(0になるはず)",answer1,answer2)
print("以下，プラスの方を有理化してから計算した結果")
x3=-4.0*c/(2.0*(b+np.sqrt(b**2-4.0*c)))
print("x3 =",x3)
answer3=x3**2+b*x3+c
print("得られた解を代入した結果(0になるはず)",answer1,answer3)
