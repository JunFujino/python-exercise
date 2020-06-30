import numpy as np
s=0
i=1
print("解析解",(np.pi**2)/6)
n=np.power(10,4)
while i<n+1:
  s=s+1/i**2
  if i%1000==0:
    print(i)
    print("数値解",s) 
  i=i+1
