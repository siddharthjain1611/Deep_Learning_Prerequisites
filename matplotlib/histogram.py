from scatterplot import *

# discrized probability distribution of data / the frequency counts in each bucket of values

# it show how many points in x fall into each bucket

plt.hist(x)
plt.show()

# to see random distribution
# create an array of 10 elements by default

R = np.random.random(10000)

plt.hist(R)
plt.show()

# let set 20 buckets

plt.hist(R, bins = 20)
plt.show()

# linear regression where all elements are normally distributed

y_act = 2*x + 1
residuals = y - y_act

plt.hist(residuals)
plt.show()
