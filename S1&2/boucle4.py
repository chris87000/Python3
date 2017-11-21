import numpy as np
import matplotlib.pyplot as plt
# coding: utf-8

def morceaux(x):
    if x <= -5:
        return x * (-1) -5
    elif x > -5 and x < 5:
        return 0
    else:
        return x /5 -1
    return       

# un echantillon des X entre -10 et 20
X = np.linspace(-10, 20)

# et les Y correspondants
Y = np.vectorize(morceaux)(X)

# on n'a plus qu'a dessiner
plt.plot(X, Y)
plt.show()