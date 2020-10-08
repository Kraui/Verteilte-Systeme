import numpy as np
import matplotlib.pyplot as plt

d, n = 100, 50  # Pixeldichte & Anzahl der Iterationen
r = 2.5  # Fluchtradius (muss größer als 2 sein)

x = np.linspace(-2.5, 1.5, 4 * d + 1)
y = np.linspace(-1.5, 1.5, 3 * d + 1)

A, B = np.meshgrid(x, y)
C = A + B * 1j

Z = np.zeros_like(C)
T = np.zeros(C.shape)

for k in range(n):
    M = abs(Z) < r
    Z[M] = Z[M] ** 2 + C[M]
    T[M] = k + 1

plt.imshow(T, cmap=plt.cm.twilight_shifted)
plt.savefig("mandelbrot.png", dpi=200)