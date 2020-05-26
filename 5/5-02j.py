import matplotlib.pyplot as plt
a=1
b=0
plt.scatter(a,b,s=5,c="blue")
itr=200 #繰り返し回数
for n in range(1,itr+1):
    ap = a
    bp = b 
    a = 0.90 * ap + 0.2 * bp
    b = -0.10 * ap + 1.10 * bp
    plt.scatter(a,b,s=5,c="blue")
plt.show()