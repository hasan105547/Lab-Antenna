"""Lab 5: 2D Radiation Pattern of a Broadside 3-Element Array Antenna"""
import numpy as np
import matplotlib.pyplot as plt

N = 3
d = 0.5      # lambda/2
beta = 0     # broadside => zero phase difference

phi = np.linspace(0, 2 * np.pi, 721)
psi = 2 * np.pi * d * np.cos(phi) + beta

AF = np.abs(sum(np.exp(1j * n * psi) for n in range(N)))
AF = AF / AF.max()

ax = plt.subplot(111, projection="polar")
ax.plot(phi, AF, linewidth=2)
ax.set_title("Broadside 3-Element Array (d=λ/2)", pad=20)
plt.show()