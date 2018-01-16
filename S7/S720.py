import numpy as np
import matplotlib.pyplot as plt

array = np.array([12, 25, 32, 55])
print(array)

try:
    array = np.array(1, 2, 3, 4)
except Exception as e:
    print(f"OOPS, {type(e)}, {e}")
    
builtin_range = np.array(range(10))
print(builtin_range)

numpy_range = np.arange(10)
print(numpy_range)

numpy_range_f = np.arange(1.0, 2.0, 0.1)
print(numpy_range_f)

X = np.linspace(0., 10., 20)
print(X)

Y = np.cos(X)
plt.plot(X, Y);
#plt.show()

Z = np.cos(X)**2 + np.sin(X)**2 + 3

plt.plot(X, Z);
#plt.show()

# le décorateur np.vectorize vous permet
# de facilement transformer une opération scalaire
# en opération vectorielle
# je choisis à dessein une fonction définie par morceaux
@np.vectorize
def scalar_function(x):
    return x**2 + 2*x + (1 if x <=0 else 10)
# je choisis de prendre beaucoup de points
# à cause de la discontinuité
X = np.linspace(-5, 5, 1000)
Y = scalar_function(X)
plt.plot(X, Y);
plt.show()
