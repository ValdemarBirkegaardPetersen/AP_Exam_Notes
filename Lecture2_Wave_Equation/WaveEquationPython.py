import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
plt.style.use('dark_background')

fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.add_subplot(1,1,1)

#Wave speed (c)
c = 1

#x-axis
x0 = np.linspace(-pi,pi,10000)

#inital time 
t0 = 0

#Time increment
dt = 0.05


#Wave equation solution
def waveEq(x, t):
    return 0.5*(np.sin(x-c*t) + np.sin(x+c*t))

a = []

for i in range(500):
    value = waveEq(x0, t0)
    t0 = t0 + dt
    a.append(value)
    
k = 0 

def animate(i):
    global k
    x = a[k]
    k += 1
    ax1.clear()
    plt.plot(x0,x,color="cyan")
    plt.grid(True)
    plt.ylim([-2,2])
    plt.xlim([-pi,pi])
    
anim = animation.FuncAnimation(fig,animate,frames=360,interval=20)

plt.show()

