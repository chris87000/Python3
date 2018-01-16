import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import  Axes3D


X = np.linspace(0,10)
print(X)
Y = np.sin(X)

plt.plot(X,Y)
plt.xlabel("temps")
plt.ylabel("quasi-sinus")
plt.show()

scope=3
xs = np.linspace(-scope,scope)
ys = np.linspace(-scope,scope)

print(xs);print(ys)
X,Y = np.meshgrid(xs,ys)

Z = np.exp(-(X**2 + Y**2))

fig = plt.figure()
ax = fig.gca(projection="3d")
ax.plot_surface(X,Y,Z)
plt.show()