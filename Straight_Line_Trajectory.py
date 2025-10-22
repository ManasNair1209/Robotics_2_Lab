import numpy as np
import matplotlib
matplotlib.use('TkAgg') # For pop-up window
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# robot parameters and steps
L1, L2, L3 = 2.0, 5.0, 4.0
steps = 50 

# straight line trajectory points
P_start = np.array([6.0, 2.0, 7.0])
P_end   = np.array([5.0, 3.0, 6.0])

x_traj = np.linspace(P_start[0], P_end[0], steps)
y_traj = np.linspace(P_start[1], P_end[1], steps)
z_traj = np.linspace(P_start[2], P_end[2], steps)

# plot
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# animation
for i in range(steps):
    Px, Py, Pz = x_traj[i], y_traj[i], z_traj[i]
    
    # ik
    t1 = np.arctan2(Py, Px)
    r = np.sqrt(Px**2 + Py**2)
    s = Pz - L1
    
    
    cos_t3 = (r**2 + s**2 - L2**2 - L3**2) / (2 * L2 * L3)
    t3 = -np.arccos(cos_t3) 
    
    # Find t2
    k1 = L2 + L3 * np.cos(t3)
    k2 = L3 * np.sin(t3)
    t2 = np.arctan2(r, s) - np.arctan2(k2, k1)

    # fk
    P0 = np.array([0, 0, 0])
    P1 = np.array([0, 0, L1])
    
    P2_x = (L2 * np.sin(t2)) * np.cos(t1)
    P2_y = (L2 * np.sin(t2)) * np.sin(t1)
    P2_z = L1 + (L2 * np.cos(t2))
    P2 = np.array([P2_x, P2_y, P2_z])
    
    P3 = np.array([Px, Py, Pz]) 

    # plot
    ax.cla() 
    
    # Plot the full path
    ax.plot(x_traj, y_traj, z_traj, 'c--')
    
    # Plot the arm
    xs = [P0[0], P1[0], P2[0], P3[0]]
    ys = [P0[1], P1[1], P2[1], P3[1]]
    zs = [P0[2], P1[2], P2[2], P3[2]]
    ax.plot(xs, ys, zs, 'k-', marker='o') 
    
    # Add one line of plot limits to stop it from jumping
    ax.set_xlim(-8, 8); ax.set_ylim(-8, 8); ax.set_zlim(0, 11)
    
    plt.draw()
    time.sleep(0.05)

plt.ioff()
plt.show()