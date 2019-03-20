# Gaussian distribution (normal distribution ) is a very common continuous probability distribution
# scipy is a fast way to calculate

from scipy.stats import norm
import numpy as np

# probability density of a zero from standart normal
norm.pdf(0)

# if mean = 5 and standart devation = 10
norm.pdf(0, loc = 5, scale = 10)

# to calculate the probability densities of many diff-t values
# 1st) create an array
r = np.random.randn(10)

# 2nd) calculate the pdf of all values stored in array at the same time
norm.pdf(r)

# we can calculate lognorm
norm.logpdf(r)

# cumulative distribution function (CDF)
# this is the integral of the PDAF from -inf to x
norm.cdf(r)

# and also log CDF
norm.logcdf(r)
