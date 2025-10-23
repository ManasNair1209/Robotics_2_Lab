import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters 
L1 = 5.0  # link1 length
L2 = 4.0  # link2 length

# Goal joint values
t1_deg = 30.0   
t2_deg = 60.0   
d3 = 3.0      

# degrees to radians conversion
t1 = np.deg2rad(t1_deg)
t2 = np.deg2rad(t2_deg)

# Fk main 

# Base is in orgin 
P0 = np.array([0.0, 0.0, 0.0])

P1_x = L1 * np.cos(t1)
P1_y = L1 * np.sin(t1)
P1_z = 0.0
P1 = np.array([P1_x, P1_y, P1_z])

P2_x = L1*np.cos(t1) + L2*np.cos(t1 + t2)
P2_y = L1*np.sin(t1) + L2*np.sin(t1 + t2)
P2_z = 0.0
P2 = np.array([P2_x, P2_y, P2_z])

P3_x = P2_x
P3_y = P2_y
P3_z = -d3  
P3 = np.array([P3_x, P3_y, P3_z])


# Result Values
print(f"Robot Joints: t1={t1_deg} deg, t2={t2_deg} deg, d3={d3}")
print(f"Final Hand Position (X,Y,Z): ({P3[0]:.2f}, {P3[1]:.2f}, {P3[2]:.2f})")

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs = [P0[0], P1[0], P2[0], P3[0]]
ys = [P0[1], P1[1], P2[1], P3[1]]
zs = [P0[2], P1[2], P2[2], P3[2]]

ax.plot(xs, ys, zs, 'bo-')

# Add labels to make it clear
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Simple SCARA Robot FK')
ax.set_box_aspect([1,1,1]) 

plt.show()
