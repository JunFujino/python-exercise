import numpy as np
x=9
print("(i)  ",np.sqrt(x+1)-np.sqrt(x))
y=np.power(10,14)
print("(ii) ",np.sqrt(y+1)-np.sqrt(y))
print("(iii)",5/np.power(10,8))
print("桁落ちによる誤差は",np.sqrt(y+1)-np.sqrt(y)-5/np.power(10,8))
