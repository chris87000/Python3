import string
import numpy as np
import matplotlib.pyplot as plt
# coding: utf-8

def P(x):
    return 2 * x *x -3 * x -2

def liste_P(liste_x):
    polynome=[]
    for x in liste_x:
        y = P(x)
        polynome.append(y)
        
    return polynome

# un echantillon des X entre -10 et 10
X = np.linspace(-10, 10)

# et les Y correspondants
Y = liste_P(X)
# on n'a plus qu'� dessiner
plt.plot(X, Y)
plt.show()