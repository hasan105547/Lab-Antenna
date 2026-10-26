"""Lab 3: 3D Radiation Pattern of a Horn Antenna (rectangular aperture model)"""
import numpy as np
import matplotlib.pyplot as plt

lam = 1.0
a, b = 3 * lam, 2 * lam   # aperture width and height

theta = np.linspace(0, np.pi, 150)
phi = np.linspace(0, 2 * np.pi, 150)
TH, PH = np.meshgrid(theta, phi)

# Aperture field pattern (sinc in both planes) x obliquity factor
E = np.abs(np.sinc(a / lam * np.sin(TH) * np.cos(PH)) *
           np.sinc(b / lam * np.sin(TH) * np.sin(PH)) *
           (1 + np.cos(TH)) / 2)
E[TH > np.pi / 2] = 0   # radiates only forward

x = E * np.sin(TH) * np.cos(PH)
y = E * np.sin(TH) * np.sin(PH)
z = E * np.cos(TH)

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(x, y, z, cmap="jet", edgecolor="none")
ax.set_title("3D Radiation Pattern of a Horn Antenna")
ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
plt.show()
