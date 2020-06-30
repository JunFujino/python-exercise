from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
G = 9.8   # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg

def derivs(x):
    F = np.zeros_like(x)
    F[0] = x[1]
    delta = x[2] - x[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    F[1] = ((M2 * L1 * x[1] * x[1] * sin(delta) * cos(delta)
                + M2 * G * sin(x[2]) * cos(delta)
                + M2 * L2 * x[3] * x[3] * sin(delta)
                - (M1+M2) * G * sin(x[0]))
               / den1)
    F[2] = x[3]
    den2 = (L2/L1) * den1
    F[3] = ((- M2 * L2 * x[3] * x[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(x[0]) * cos(delta)
                - (M1+M2) * L1 * x[1] * x[1] * sin(delta)
                - (M1+M2) * G * sin(x[2]))
               / den2)
    return F

dt = 0.0001
N=100000
# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0 #- 0.010 (case1)
w2 = 0.0
dth = 0.010     # error
# initial conditions
x = np.radians([th1, w1, th2, w2])
y = np.radians ([th1,w1,th2+dth,w2])
xh = np.zeros((N,4))
yh = np.zeros((N,4))
for i in range(N):
    x = x + derivs(x)*dt
    xh[i,:]=x[:]
    y = y + derivs(y)*dt
    yh[i,:]=y[:]
t = np.arange(0, int(dt*N), dt)
#plt.plot(t,xh[:,0],c="red")
#plt.plot(t,xh[:,2],c="blue")
#plt.plot(t,yh[:,0],c="yellow")
#plt.plot(t,yh[:,2],c="green")
plt.plot(t,np.log( np.abs(xh[:,0]-yh[:,0]) ),c="red")
plt.plot(t,np.log( np.abs(xh[:,2]-yh[:,2]) ),c="blue")
plt.xlabel('t')
plt.show()