# spherical Gaussian (each dim os uncorrelated and independent to the other)
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

r = np.random.randn(10000, 2)

# spread out in a circular cloud
plt.scatter(r[:,0], r[:,1])
plt.show()

# elliptical Gaussian
r[:,1] = 5*r[:,1] + 2
plt.scatter(r[:,0], r[:,1])
plt.axis('equal') # for data with each axis equal together
plt.show()
