"""Lab 9: 2D Radiation Pattern of a Broadside 5-Element Array Antenna"""
import numpy as np
import matplotlib.pyplot as plt

N = 5
d = 0.5      # lambda/2
beta = 0     # broadside

phi = np.linspace(0, 2 * np.pi, 721)
psi = 2 * np.pi * d * np.cos(phi) + beta

AF = np.abs(sum(np.exp(1j * n * psi) for n in range(N)))
AF = AF / AF.max()

ax = plt.subplot(111, projection="polar")
ax.plot(phi, AF, linewidth=2)
ax.set_title("Broadside 5-Element Array (d=λ/2)", pad=20)
plt.show()