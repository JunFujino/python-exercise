import numpy as np
print("係数を入力")
a = list(map(float,input().split()))
b=a[0]
c=a[1]
def solution(b,c):
  x1=(-b-np.sqrt(b**2-4*c))/2.0
  x2=-2*c/(b+np.sqrt(b**2-4*c))
  return x1,x2
s1, s2=solution(b,c)
print("解1",s1,"解2",s2)
