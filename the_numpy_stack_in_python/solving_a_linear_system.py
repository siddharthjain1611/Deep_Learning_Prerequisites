# Problem : Ax = b
# Solution : A^(-1)Ax = x = A^(-1)b

import numpy as np

A = np.array([[1,2],[3,4]])

b = np.array([1,2])

# solve for x

x = np.linalg.inv(A).dot(b)

# or

x = np.linalg.solve(A,b)
