import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# parameters
L1, L2 = 5.0, 4.0  
steps = 50 

# straight line trajectory points
P_start = np.array([6.0, 2.0, -1.0]) 
P_end   = np.array([3.0, 5.0, -4.0]) 

x_traj = np.linspace(P_start[0], P_end[0], steps)
y_traj = np.linspace(P_start[1], P_end[1], steps)
z_traj = np.linspace(P_start[2], P_end[2], steps)

# plot
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# loop
for i in range(steps):
    Px, Py, Pz = x_traj[i], y_traj[i], z_traj[i]
    
    # IK
    # Solve d3 (prismatic joint)
    d3 = -Pz 
    cos_t2_num = Px**2 + Py**2 - L1**2 - L2**2
    cos_t2_den = 2 * L1 * L2
    if abs(cos_t2_num / cos_t2_den) > 1:
        print(f"Skipping unreachable point ({Px:.1f}, {Py:.1f})")
        continue # Skip this step
        
    t2 = -np.arccos(cos_t2_num / cos_t2_den) 
    k1 = L1 + L2 * np.cos(t2)
    k2 = L2 * np.sin(t2)
    t1 = np.arctan2(Py, Px) - np.arctan2(k2, k1)

    # plot
    P0 = np.array([0, 0, 0]) 
    
    P1_x = L1 * np.cos(t1)
    P1_y = L1 * np.sin(t1)
    P1 = np.array([P1_x, P1_y, 0])
    P2 = np.array([Px, Py, 0])
    P3 = np.array([Px, Py, Pz]) 

    # plot
    ax.cla() 
    ax.plot(x_traj, y_traj, z_traj, 'c--')
    
    # Plot the arm
    xs = [P0[0], P1[0], P2[0], P3[0]]
    ys = [P0[1], P1[1], P2[1], P3[1]]
    zs = [P0[2], P1[2], P2[2], P3[2]]
    ax.plot(xs, ys, zs, 'k-', marker='o') 
    
    # Add plot limits for SCARA
    ax.set_xlim(-10, 10); ax.set_ylim(-10, 10); ax.set_zlim(-5, 5)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    
    plt.draw()
    time.sleep(0.05)

plt.ioff()
plt.show()
