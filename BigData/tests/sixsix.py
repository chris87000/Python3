import numpy as np
import matplotlib.pyplot as plt
from numpy import random


v = np.arange(5, dtype=int)
print(v)

print("****"*3)
mask = np.array([True, False, True, False, False])
print(v[mask])
print(v[[0, 2]])

print(v > 2)
print(v[v > 2])

print("****"*3)
A = np.array([[n + m * 10 for n in range(4)]  for m in range(4)])
print(A)
print("****"*3)
print(A.T)

print("****"*3)
(A + A.T) / 2  # addition terme-à-terme
print("****"*3)
print(np.trace(A))  # trace de A
print(A.shape)
print(A * A)  # multiplication élément par élément
print(np.dot(A, A))  # multiplication de matrices
print(v)
print(np.dot(A, v[:4]))  # OK

print("**** INV Matrice"*3)
B = random.standard_normal((3, 3))
print(B)
Binv = np.linalg.inv(B)
print(Binv)
print(np.dot(B, Binv))