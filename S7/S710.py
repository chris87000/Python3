import random
import math
import timeit
import numpy as np

start = timeit.default_timer()

size=10**4

l = [random.random() for i in range(size)]

print(l)

[math.cos(x) for x in l]
stop = timeit.default_timer()

print (stop - start)

n = np.array(l)
print(type(n))
np.cos(n)
stop2 = timeit.default_timer() 


print (stop2 - start) 

