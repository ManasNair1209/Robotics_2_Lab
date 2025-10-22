import numpy as np
import matplotlib
matplotlib.use('TkAgg') #used for the pop up window
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters 
L1 = 2.0 
L2 = 5.0  
L3 = 4.0  

# Set the goal angles
t1_deg = 90.0   
t2_deg = 45.0   
t3_deg = -30.0  

# deg to radians
t1 = np.deg2rad(t1_deg)
t2 = np.deg2rad(t2_deg)
t3 = np.deg2rad(t3_deg)

# Fk main 

# base
P0 = np.array([0.0, 0.0, 0.0])
P1 = np.array([0.0, 0.0, L1])

P2_x = (L2 * np.sin(t2)) * np.cos(t1)
P2_y = (L2 * np.sin(t2)) * np.sin(t1)
P2_z = L1 + (L2 * np.cos(t2))
P2 = np.array([P2_x, P2_y, P2_z])

P3_x = (L2*np.sin(t2) + L3*np.sin(t2+t3)) * np.cos(t1)
P3_y = (L2*np.sin(t2) + L3*np.sin(t2+t3)) * np.sin(t1)
P3_z = L1 + L2*np.cos(t2) + L3*np.cos(t2+t3)
P3 = np.array([P3_x, P3_y, P3_z])

# Result Values
print(f"Robot Angles (deg): t1={t1_deg}, t2={t2_deg}, t3={t3_deg}")
print(f"Final Hand Position (X,Y,Z): ({P3[0]:.2f}, {P3[1]:.2f}, {P3[2]:.2f})")

# --- 4. Plot ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Combine all points into X, Y, Z arrays
xs = [P0[0], P1[0], P2[0], P3[0]]
ys = [P0[1], P1[1], P2[1], P3[1]]
zs = [P0[2], P1[2], P2[2], P3[2]]

# Plot the whole arm in one command: 'bo-' means blue dots + solid line
ax.plot(xs, ys, zs, 'bo-')

plt.show()