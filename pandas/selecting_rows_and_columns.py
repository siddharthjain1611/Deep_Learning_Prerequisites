# import previous file to continue

from dataframes import *

# convert the data frame into matrix

M = X.as_matrix()
type(M) # returns numpy array

# Numpy X[0] gives 0th row
# Pandas X[0] gives column that has name 0

# to see 0 with row 1
X.iloc[0]
X.ix[0] # also a series

# to see zero and second columns

X[[0,2]]

# to find rows by special criteria
# like finding all the rows where the data for the 0 column is < 5

X[ X[0] < 5 ]

# if we go straight we get booleans

X[0] < 5
