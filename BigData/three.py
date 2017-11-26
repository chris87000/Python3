import numpy as np
import matplotlib.pyplot as plt
from numpy import random

a = np.arange(5, dtype=float)
print(a)
print(a + 1)
print(2 * a)
print(a ** 2)
print("****************"*2)
a = np.array([1, 2], dtype=np.int64)
b = np.array([2, 2], dtype=np.int64)
print(a / b)
a = np.array([1, 2], dtype=float)
b = np.array([2, 2], dtype=float)
print(a / b)
print(a // b)

print("****************"*2)
print(random.random_sample((3, 3)))

print(random.standard_normal((3, 3))) 
a = random.standard_normal(10000)
hh = plt.hist(a, 40)
plt.show()

print("****************"*2)
C = random.standard_normal((32, 32))
print(C.shape)
plt.imshow(C, interpolation='nearest')
plt.colorbar()
plt.show()
print("****************"*2)