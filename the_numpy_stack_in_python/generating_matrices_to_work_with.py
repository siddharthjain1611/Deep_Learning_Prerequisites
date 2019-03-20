import numpy as np

# create zero matrix with a size 10x10
zeros = np.zeros((10,10))

# create ones matrix with a size 10x10
ones = np.ones((10,10))

# create matrix with random numbers ( >0 and <1 )

random_matrix = np.random.random((10,10))

# create Gaussian distributed numbers

gaussian = np.random.randn(10,10)

# calculate the averahe of the gaussian

gaussian.mean()
