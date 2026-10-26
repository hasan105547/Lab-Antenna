"""Lab 6: Far-field pattern of two isotropic point sources,
equal amplitude and equal phase (d = lambda/2)"""
import numpy as np
import matplotlib.pyplot as plt

d = 0.5          # lambda/2
phi = np.linspace(0, 2 * np.pi, 721)

# E = |cos(pi*d*cos(phi))| for equal amp & phase
E = np.abs(np.cos(np.pi * d * np.cos(phi)))

ax = plt.subplot(111, projection="polar")
ax.plot(phi, E, linewidth=2)
ax.set_title("Two Isotropic Sources: Equal Amp & Phase (d=λ/2)\nBroadside pattern", pad=20)
plt.show()