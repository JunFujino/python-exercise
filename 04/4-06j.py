import matplotlib.pyplot as plt
n=100
c=-0.835-0.1j
for ix in range(-n,n):
  x=2*ix/n
  for iy in range(-n,n):
    y=2*iy/n
    z=complex(x,y)
    itr=1000
    for i in range(itr):
      z=z**2+c
      if (abs(z)>2.0):
        break
    if(i==itr-1):
      plt.scatter(x,y,s=5,c="blue")
plt.show()    