# Helps to load data and convert it into Numpy array

import pandas as pd

X = pd.read_csv('data_2d.csv', header = None)

type(X) # data frame

X.info() # to see the information about data frame

X.head(10) # show first 10 rows
