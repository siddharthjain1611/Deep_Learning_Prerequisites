# Loading in data
# DL and ML learning from data, so that's why we need data loading to be an automatic reflex

# CSV - comma separated values ( tables, so it can be opened in Excel )
# We gonna use data_2d.csv file (100x3 matrix)

import numpy as np

x_list = []

for line in open('data_2d.csv'):
    row = line.split(',')
    sample = map(float, row)
    x_list.append(sample)

x_list = np.array(x_list)
np.shape(x_list)
