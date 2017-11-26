import numpy as np
import matplotlib.pyplot as plt

x = np.array(range(0, 10, 2)) # à partir d'une liste
print(x)
print("\n")
x = np.arange(0, 10, 2) # OK : plus efficace
print(x)
x = np.arange(-1, 1, 0.5)  # avec flottants
print("\n")
x = np.arange(0, 10, 2) # OK : plus efficace
print(x)
print("\n")
x = np.arange(-1, 1, 0.5)  # avec flottants
print(x)
print("\n")
# avec linspace, le début et la fin SONT inclus
np.linspace(0, 10, 6)

print("******** Linspace********"*2)
t = np.linspace(0, 10, 6)
print(t)
print("\n")
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='$y = \sin(x)$')
plt.legend()
plt.show()