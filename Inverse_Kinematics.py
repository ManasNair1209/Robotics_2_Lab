import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# parameters and target values
L1, L2 = 5.0, 4.0  
Px, Py, Pz = 6.0, 2.0, -3.0 

# IK
d3 = -Pz 
cos_t2_num = Px**2 + Py**2 - L1**2 - L2**2
cos_t2_den = 2 * L1 * L2
t2 = -np.arccos(cos_t2_num / cos_t2_den) 


k1 = L1 + L2 * np.cos(t2)
k2 = L2 * np.sin(t2)
t1 = np.arctan2(Py, Px) - np.arctan2(k2, k1)

# print results
print(f"Target (X,Y,Z): ({Px}, {Py}, {Pz})")
print("Calculated Joint Values")
print(f"t1 (Base):   {np.rad2deg(t1):.2f} degrees")
print(f"t2 (Elbow):  {np.rad2deg(t2):.2f} degrees")
print(f"d3 (Z-axis): {d3:.2f} units") # d3 is the joint value

# plot
P0 = np.array([0.0, 0.0, 0.0]) 

P1_x = L1 * np.cos(t1)
P1_y = L1 * np.sin(t1)
P1 = np.array([P1_x, P1_y, 0.0]) 

P2 = np.array([Px, Py, 0.0]) 

P3 = np.array([Px, Py, Pz]) 

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs = [P0[0], P1[0], P2[0], P3[0]]
ys = [P0[1], P1[1], P2[1], P3[1]]
zs = [P0[2], P1[2], P2[2], P3[2]]

ax.plot(xs, ys, zs, 'k-', marker='o') 
ax.scatter(Px, Py, Pz, color='red', marker='X', s=200)

ax.set_box_aspect([1,1,1]) 
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
