import numpy as np
import matplotlib.pyplot as plt
from numpy import random


A = np.array([[n + m * 10 for n in range(4)]  for m in range(4)])
print(A)
print(np.sum(A))  # somme de tous les éléments

print(np.sum(A[1, :]))  # somme de la 2ième ligne

print(np.sum(A, axis=1))  # somme de toutes les lignes

print(np.sum(A, axis=0))  # somme de toutes les colonnes

print(np.mean(A))  # moyenne de tous les éléments

print(np.mean(A[1, :]))  # moyenne de la 2ième ligne

print(np.mean(A, axis=1))  # moyenne de toutes les lignes

print(np.mean(A, axis=0))  # moyenne de toutes les colonnes

print(np.max(A, axis=0))  # maximum de toutes les colonnes