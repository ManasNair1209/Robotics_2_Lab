import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Parameters & Target ---
L1, L2, L3 = 2.0, 5.0, 4.0
Px, Py, Pz = 6.0, 2.0, 7.0

# --- 2. INVERSE KINEMATICS (Raw Calculation) ---
t1 = np.arctan2(Py, Px)
r = np.sqrt(Px**2 + Py**2)
s = Pz - L1
t3 = -np.arccos( (r**2 + s**2 - L2**2 - L3**2) / (2 * L2 * L3) )
k1 = L2 + L3 * np.cos(t3)
k2 = L3 * np.sin(t3)
t2 = np.arctan2(r, s) - np.arctan2(k2, k1)

# --- 3. PRINT THE CALCULATED VALUES (in degrees) ---
print(f"Target (X,Y,Z): ({Px}, {Py}, {Pz})")
print("--- Calculated Angles (degrees) ---")
print(f"t1 (Waist):   {np.rad2deg(t1):.2f}")
print(f"t2 (Shoulder): {np.rad2deg(t2):.2f}")
print(f"t3 (Elbow):    {np.rad2deg(t3):.2f}")

# --- 4. FORWARD KINEMATICS (for plotting) ---
P0 = np.array([0.0, 0.0, 0.0])
P1 = np.array([0.0, 0.0, L1])
P2_x = (L2 * np.sin(t2)) * np.cos(t1)
P2_y = (L2 * np.sin(t2)) * np.sin(t1)
P2_z = L1 + (L2 * np.cos(t2))
P2 = np.array([P2_x, P2_y, P2_z])
P3 = np.array([Px, Py, Pz]) # The hand position is the target

# --- 5. Plot (Minimal) ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Combine all arm points into X, Y, Z arrays
xs = [P0[0], P1[0], P2[0], P3[0]]
ys = [P0[1], P1[1], P2[1], P3[1]]
zs = [P0[2], P1[2], P2[2], P3[2]]

# Plot the arm
ax.plot(xs, ys, zs, 'k-', marker='o') 
# Plot the target
ax.scatter(Px, Py, Pz, color='red', marker='X', s=200)

# Set equal scaling
ax.set_box_aspect([1,1,1]) 
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()