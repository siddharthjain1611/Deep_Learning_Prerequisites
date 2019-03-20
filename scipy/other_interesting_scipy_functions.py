# small tour

import numpy as np
import matplotlib.pyplot as plt

# Fourier transform it converts the signal from the time domain into tthe frequency domain
# freq-compunents of the original signal
x = np.linspace(0,100,10000)

y = np.sin(x) + np.sin(3*x) + np.sin(5*x)

plt.plot(y)
plt.show()

# Fast Forirer Transform
Y = np.fft.fft(y)

plt.plot(Y)
plt.show()
