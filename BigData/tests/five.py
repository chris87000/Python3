import numpy as np
import matplotlib.pyplot as plt
from numpy import random

v = np.array([1, 3, 2, 4])
M = np.array([[1, 2], [3, 4]])

# v ndarray à 1 dimension -> un indice
print(v[0])
# M ndarray à 2 dimensions -> deux indices 
print(M[1, 0])
print(M[0])  # La première ligne
print(M[1, :])  # 2 ème ligne (indice 1)
print(M[:, 1])  # 2 ème colonne (indice 1)

print("****************"*2)
print(M)
M[1, :] = -1  # assigne d'un élément à toute une ligne
print(M)
M[:, 1] = [5, 6]  # assignement de plusieurs éléments
print(M)

print("******** Slicing ********"*2)
A = np.array([1, 2, 3, 4, 5])
print(A)
print(A[1:3])
print(A[::])
print(A[::2]) # step = 2
print(A[:3]) # les trois premiers éléments
print(A[3:]) # à partir de l'indice 3
A = np.array([1, 2, 3, 4, 5])
print(A[-1]) # le dernier élément

print("******** Slicing 2/3D ********"*2)
A = np.array([[n + m * 10 for n in range(4)]  for m in range(4)])
print(A)
# un bloc du tableau
print(A[1:3, 1:3])
print(A[::2, ::2])  # 1 ligne sur 2 et 1 colonne sur 2

print("******** Slicing 2/3D : indices********"*2)
indices = [1, 3]
print(A[indices])  # lignes d'indices 1 et 3

indices = [1, 3]
print(A[:, indices])  # colonnes d'indices 1 et 3
print("\n")
# sous-tableau lignes [0,1] et colonnes [2,3]
print (A[np.ix_([0, 2], [1, 3])])


# éléments d'indices [0,1] et [2,3]
print(A[[0, 2], [1, 3]])





