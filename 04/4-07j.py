def wa(a,b):
  c=a+b
  return c
def seki(a,b):
  c=a*b
  return c
def sa(a,b):
  c=a-b
  return c
print("2つの数字を入力")
a = list(map(float,input().split()))  #標準入力
print("和",wa(a[0],a[1]))   
print("積",seki(a[0],a[1]))
print("差",sa(a[0],a[1]))
