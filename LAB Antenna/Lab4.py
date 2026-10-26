"""Lab 4: 2D Radiation Pattern of a Linear Antenna Array"""
import numpy as np
import matplotlib.pyplot as plt

N = 4            # number of elements
d = 0.5          # spacing in wavelengths
beta = 0         # progressive phase (0 = broadside)

phi = np.linspace(0, 2 * np.pi, 721)
k = 2 * np.pi
psi = k * d * np.cos(phi) + beta

AF = np.zeros_like(phi, dtype=complex)
for n in range(N):
    AF += np.exp(1j * n * psi)
AF = np.abs(AF)
AF = AF / AF.max()

ax = plt.subplot(111, projection="polar")
ax.plot(phi, AF, linewidth=2)
ax.set_title(f"2D Pattern of Linear Array (N={N}, d=λ/2)", pad=20)
plt.show()