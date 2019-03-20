import numpy as np

# --- for loop
a = np.array([1,2])
b = np.array([2,1])

dot = 0

for e,f in zip(a,b):
    dot += e*f

dot # result of dot product

# --- dot function
# several ways to calculate
np.sum(a*b)
(a*b).sum()
a.dot(b)

# --- length of a vector

amog = np.sqrt((a*a).sum())
# or you can do
amog = np.linalg.norm(a)

# --- cosine method

cos_angle = a.dot(b)/(np.linalg.norm(a) * np.linalg.norm(b))
angle = np.arccos(cos_angle)
