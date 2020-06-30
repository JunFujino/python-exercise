import numpy as np
s=0
n=np.power(10,4)
for i in range(1,n+1):
  s=s+1/i**2
print("数値解",s)
print("解析解",(np.pi**2)/6) 
s=0
n=np.power(10,5)
for i in range(1,n+1):
  s=s+1/i**2
print("数値解",s)
print("解析解",(np.pi**2)/6) 
s=0 
n=np.power(10,5)
for i in range(1,n+1):
  s=s+1/i**2  
print("数値解",s) 
print("解析解",(np.pi**2)/6)
