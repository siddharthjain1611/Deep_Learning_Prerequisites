from gaussian_pdf_and_cdf import *
import matplotlib.pyplot as plt

# discuss sampling from a Gaussian more in depth
# show histogram to verify it's standart normal
r = np.random.randn(10000)
plt.hist(r, bins = 100)
plt.show()

# what if we have an arbitary mean and standart deviation (deviation = 10 and
#                                                                    mean = 5)
r = 10 * np.random.randn(10000) + 5
plt.hist(r, bins = 100)
plt.show()
