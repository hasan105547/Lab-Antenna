"""Lab 1: 3D Radiation Pattern of Half-Wave Dipole Antenna"""
import numpy as np
import matplotlib.pyplot as plt
 
theta = np.linspace(0.001, np.pi - 0.001, 100)
phi = np.linspace(0, 2 * np.pi, 100)
TH, PH = np.meshgrid(theta, phi)
 
# Half-wave dipole: E(theta) = cos(pi/2 * cos(theta)) / sin(theta)
E = np.abs(np.cos(np.pi / 2 * np.cos(TH)) / np.sin(TH))
 
x = E * np.sin(TH) * np.cos(PH)
y = E * np.sin(TH) * np.sin(PH)
z = E * np.cos(TH)
 
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(x, y, z, cmap="jet", edgecolor="none")
ax.set_title("3D Radiation Pattern of Half-Wave Dipole Antenna")
ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
plt.show()