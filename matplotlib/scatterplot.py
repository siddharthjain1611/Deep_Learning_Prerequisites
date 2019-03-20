from line_chart import *
import pandas as pd

# add table and represent it as matrix

A = pd.read_csv('data_1d.csv', header = None).as_matrix()

# x-axis is the 1st column and y-axis is the 2nd column

x = A[:,0]
y = A[:,1]

plt.scatter(x, y)

# to see whether the line is a good fit

x_line = np.linspace(0, 100, 100)
y_line = 2 * x_line + 1

plt.plot(x_line, y_line)

plt.show()
