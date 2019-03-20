# sample from a general multivariate distribution
# dim-s are not necessarily independent from each other

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as mvn

# define a covariance matrix

cov = np.array([[1, 0.8],
               [0.8, 3]])

# mean is
mn = np.array([0,2])

# random values
r = mvn.rvs(mean = mn, cov = cov, size = 1000)

plt.scatter(r[:,0],r[:,1])
plt.axis('equal')
plt.show()
