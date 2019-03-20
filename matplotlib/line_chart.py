# Matplotlib is for data visualization

import matplotlib.pyplot as plt
import numpy as np

# create data points for x-axis

x = np.linspace(0,10,10) # goes from 0 to 10 with 10 points between them

# create sin wave/ this operation is element by element

y = np.sin(x)

# we can add x-,y- and title- labels

plt.xlabel('Time')
plt.ylabel('Time function')
plt.title('Plot of sin-function')

# now it can be plotted

plt.plot(x, y)
plt.show()

# it's necessary to remember is that all computation is descrete
# so to make it look more accurate we can add more points between start and end

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()

# now it looks much smoother
