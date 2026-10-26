"""Lab 8: Far-field pattern of two isotropic point sources,
unequal amplitude and opposite phase (d = lambda/2)"""
import numpy as np
import matplotlib.pyplot as plt

d = 0.5          # lambda/2
A1, A2 = 1.0, 0.5   # unequal amplitudes
phase = np.pi       # opposite phase

phi = np.linspace(0, 2 * np.pi, 721)
psi = 2 * np.pi * d * np.cos(phi)

E = np.abs(A1 + A2 * np.exp(1j * (psi + phase)))
E = E / E.max()

ax = plt.subplot(111, projection="polar")
ax.plot(phi, E, linewidth=2)
ax.set_title("Two Isotropic Sources: Unequal Amp (1:0.5), Opposite Phase (d=λ/2)", pad=20)
plt.show()
