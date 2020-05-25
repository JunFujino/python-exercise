def max(a,b):
  if a>b:
    return a
  elif a<b:
    return b
  else:
    return (a+b)/2
print("2つの数字を入力")
a = list(map(float,input().split())) #標準入力
print(max(a[0],a[1]))
