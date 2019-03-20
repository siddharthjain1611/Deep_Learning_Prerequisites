import numpy as np
from datetime import datetime, timedelta

a = np.random.randn(100)
b = np.random.randn(100)
T = pow(10, 5) # time period

# FOR loop for dot product
def slow_dot_product(a, b):
    result = 0
    for e,f in zip(a,b):
        result += e*f

    return result

time = datetime.now() # currebt time

for t in range(T):
    slow_dot_product(a, b)

datetime_1 = datetime.now()

for i in range(T):
    a.dot(b)
datetime_2 = datetime.now() - time

print("date time 1 / date time 2 is ".format(datetime_1.total_seconds()
                                        / datetime_2.total_seconds()))
