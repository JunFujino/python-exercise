import matplotlib.pyplot as plt
a = 1
n=0
itr = 10
plt.scatter(n,a,s=5,c="blue")
for n in range(1,itr+1):
    a = 2 * a + 1
    plt.scatter(n,a,s=5,c="blue")   # 点を表示
plt.show()  #表示
