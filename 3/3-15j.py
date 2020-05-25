import numpy as np
import decimal
n=np.power(10,5)
s=0
for i in range(1,n+1):
  s=s+1
print("和",s)
s=0
for i in range(1,n+1):
  s=s+decimal.Decimal('0.10')
print("和",s)
