# Matrix products
# -- matrix multiplication
# -- requirement: inner dimensions must match
# -- if we have A of size 2x3 and B of size 3x3
# -- we can multiply AB (inner dimension is 3)
# -- we cannot multiply BA (inner dimension is 3/2)


import numpy as np

# create matrix

A = np.array([[1,2],[3,4]])

# create inverse matrix

A_inv = np.linalg.inv(A)

# identity matrix

A_int.dot(a)
A.dot(A_int)

# determinant

np.linalg.det(A)

# diagonal matrix

np.diag(A)

# to represent 2D array

np.diag([1,2])

# Outer product / Inner product

# create two vectors

a = np.array([1,2])
b = np.array([3,4])

# outer and inner product

np.outer(a,b)

np.inner(a,b)
# inner = dot 
np.dot(a,b)
a.dot(b)
b.dot(a)

# sum of diagonal elements

np.diag(A).sum()
np.trace(A)

# eigenvalues and eigenvectors

X = np.random.randn(100, 3)

# covarians (transpose it 1st)

cov = np.cov(X.T)

# operations with eigen (1st arr stores 3 eigenvalues, 2nd arr contains  eigenvectors)
np.linalg.eigh(cov)
np.linalg.eig(cov)

