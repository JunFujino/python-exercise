from numpy import sin, cos
import matplotlib.animation as animation
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
dth = 0.010
# initial conditions
j = 0  
M = 100
x = np.radians([th1, w1, th2, w2])
xh = np.zeros ((int(N/M),4))
y = np.radians ([th1,w1,th2+dth,w2])
yh = np.zeros ((int(N/M),4))
for i in range(N):
    x = x + derivs(x)*dt
    y = y + derivs(y)*dt
    if i % M == 0:      #Mステップおきに出力
        xh[j,:]=x[:]
        yh[j,:]=y[:]
        j = j + 1
#==========================================以下アニメーション用==================================================
x1 = L1*sin(xh[:, 0])
y1 = -L1*cos(xh[:, 0])
x2 = L2*sin(xh[:, 2]) + x1
y2 = -L2*cos(xh[:, 2]) + y1
x3 = L1*sin(yh[:, 0])
y3 = -L1*cos(yh[:, 0])
x4 = L2*sin(yh[:, 2]) + x3
y4 = -L2*cos(yh[:, 2]) + y3
fig = plt.figure ()
ax = fig.add_subplot (111,  autoscale_on=False , xlim=(-2, 2), ylim=(-2, 2))
ax.set_aspect('equal')
ax.grid()
line1 , = ax.plot([], [],'o-', lw = 2)
line2 , = ax.plot([], [],'o-', lw = 2)
time_template ='time = %.1fs'
time_text = ax.text (0.05, 0.9,'', transform=ax.transAxes)
def init ():
    line1.set_data ([], [])
    line2.set_data ([], [])
    time_text.set_text('')
    return line1, line2 , time_text
def animate(i):
    thisx1 = [0, x1[i], x2[i]]
    thisy1 = [0, y1[i], y2[i]]
    thisx2 = [0, x3[i], x4[i]]
    thisy2 = [0, y3[i], y4[i]]
    line1.set_data(thisx1 , thisy1)
    line2.set_data(thisx2 , thisy2)
    time_text.set_text(time_template % (i*dt*M))
    return line1, line2, time_text
ani = animation.FuncAnimation(fig , animate ,int(N/M),interval=dt*N, blit=True , init_func=init)
ani.save('double_pendulum_comparison.gif',writer='pillow',fps=50)
plt.show()