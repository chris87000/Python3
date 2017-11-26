import numpy as np
import matplotlib.pyplot as plt
from numpy import random


# Création d'un tableau 2D de zeros
A = np.zeros((2, 3)) # Attention: zeros(2, 3) est FAUX
print(A)
print(A.dtype)

print("****************"*2)
print(np.zeros((1, 3), dtype=int))  # ligne

print(np.zeros((3, 1), dtype=int))  # colonne

print(np.ones((3, 3)))  # tableau 3x3 de 1

# création d'une matrice diagonale
D = np.diag([1, 2, 3])
print(D)
# extraction de la diagonale
print(np.diag(D))

print("****************"*2)
data = np.genfromtxt('data.csv', delimiter=',')
print(data)
print(data.shape)


print("********* Matrix *******"*2)
M = random.standard_normal((3, 3))
print(M)
np.savetxt("random-data.csv", M, fmt=' % 2.3f', delimiter=',')
np.save("random-matrix.npy", M)
np.load("random-matrix.npy")
