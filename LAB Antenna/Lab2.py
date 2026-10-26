"""Lab 2: 3D Radiation Pattern of Isotropic Antenna"""
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
TH, PH = np.meshgrid(theta, phi)

# Isotropic: radiates equally in all directions
E = np.ones_like(TH)

x = E * np.sin(TH) * np.cos(PH)
y = E * np.sin(TH) * np.sin(PH)
z = E * np.cos(TH)

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(x, y, z, cmap="viridis", edgecolor="none")
ax.set_title("3D Radiation Pattern of Isotropic Antenna")
ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
ax.set_box_aspect([1, 1, 1])
plt.show()