import numpy as np
s=0
n=100
for i in range(n+1):
  s=s+i
a=np.power(10.0,20)
s=s+a
print("答え",s)
