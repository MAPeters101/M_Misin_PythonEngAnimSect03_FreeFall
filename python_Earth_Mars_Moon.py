import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Time array
t0=0
t_end=12
dt=0.02
t=np.arange(t0,t_end+dt,dt)

# Gravitational acceleration
g_Earth=-9.8 # [m/s^2]

# Position y arrays
n=2
y_i=100 # [m]
y_Earth=y_i+0.5*g_Earth*t**n
#np.set_printoptions(suppress=True)

# Velocity y arrays
y_Earth_velocity=n*0.5*g_Earth*t**(n-1)

# Acceleration y arrays
y_Earth_acceleration=(n-1)*g_Earth*t**(n-2)

# Create circles
def create_circle(r):
    degrees=np.arange(0,361,1)
    radians=degrees*np.pi/180
    sphere_x=r*np.cos(radians)
    sphere_y=r*np.sin(radians)
    return sphere_x,sphere_y

radius=5
sphere_x_Earth,sphere_y_Earth=create_circle(radius)

# np.set_printoptions(suppress=True)
# print(sphere_x_Earth)
# print(sphere_y_Earth)
# exit()

############################## ANIMATION ##############################
frame_amount=len(t)
width_ratio=1.2
y_f=-10 # [m]
dy=10 # [m]

def update_plot(num):
    if y_Earth[num]>radius:
        sphere_Earth.set_data(sphere_x_Earth,sphere_y_Earth+y_Earth[num])

    return sphere_Earth,

# Figure properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(3,4)

# Create object for Earth
ax0=fig.add_subplot(gs[:,0],facecolor=(0.9,0.9,0.9))
sphere_Earth,=ax0.plot([],[],'k',linewidth=3)
land_Earth=ax0.plot([-radius*width_ratio,radius*width_ratio],[-5,-5],linewidth=42)
plt.xlim(-radius*width_ratio,radius*width_ratio)
plt.ylim(y_f,y_i+dy)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(y_f,y_i+2*dy,dy))
plt.ylabel('altitude [m]')
plt.title('Earth')


plane_ani=animation.FuncAnimation(fig,update_plot,
    frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()






