import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(0, 400, 15), np.linspace(0, 400, 15))
P = 0.1*x*(1 - 0.01*x + 0.005*y)
Q = 0.03*y*(1 + 0.04*x - 0.01*y)
M = np.sqrt(P**2 + Q**2)

plt.quiver(x, y, P/M, Q/M)
plt.show()
