import numpy as np
import matplotlib.pyplot as plt
from numpy import random



A = np.array([[0,  2], [3, 4]])
print(A)

B = A  # assignation sans copie
B[0, 0] = 10  # changer B affecte A
print(B)
print(A)  # A est modifié

A = np.array([[0,  2], [3, 4]])
B[0,0] = -5  # B est modifié
print(B)

print("****"*3)
n, m = A.shape
print(n, m)
B = A.reshape((n * m,))
print(B.shape)
print(B)
print("****"*3)
B = A.reshape((n * m, 1))
print(B.shape)
print(B)

print("****"*3)
A = np.array([[1, 2], [3, 4]])
print(A)
print(np.tile(A, (1, 2))) # répéter la matrice 2 fois
B = np.array([[5, 6]])
print(np.concatenate((A, B), axis=0))
print(np.concatenate((A, B.T), axis=1))

print("****"*3)
print(np.vstack((A, B)))
print(np.hstack((A, B.T)))    
      