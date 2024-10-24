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
y_Earth=y_i+0,5*g_Earth*t**n

# Velocity y arrays
y_Earth_velocity=n*0.5*g_Earth*t**(n-1)

# Acceleration y arrays
y_Earth_acceleration=(n-1)*g_Earth*t**(n-2)

