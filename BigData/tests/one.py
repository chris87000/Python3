import numpy as np
import matplotlib.pyplot as plt



# un vecteur à partir d'une liste Python
v = np.array([1, 3, 2, 4])
#===============================================================================
# print(v)
# print(type(v))
# 
# plt.figure()
# plt.plot(v)
# plt.show()
#===============================================================================

#===============================================================================
# x = np.array([0,2,4,6])
# plt.figure()
# plt.plot(x, v, 'r--', label='vecteur')
# plt.xlabel('x')
# plt.ylabel('v')
# plt.title('Exemple titre')
# plt.legend(loc='lower right')
# plt.show()
#===============================================================================
M = np.array([[1, 3], [2, 4]])
print(M)
print(M[0, 0])
print(M[1, 1])
print("****************"*2)
print(v.shape)
print(M.shape)
print(type(M.shape))

print(v.ndim, ", ", M.ndim)
print(v.size, ", ", M.size)

print("************* 3D ************"*2)
T = np.array([[[1, 3, 2, 4]]])
print(T)
print(T.shape)
print(T.ndim)
print(T.size)
np.size(T)

print("****************"*2)
print(M.dtype)
m = M.itemsize # nombre d'octets par élément
n = M.nbytes # nombre d'octets
d = M.nbytes / M.size  # égal à itemsize

print(m, ", ", n, ", ", d)
M[0,0] = -1
print(M)

print("****************"*2)
a = np.array([0, 0, 0])
print(a.dtype)
a[0] = 3.2  # perte de précision
print(a)

a = np.array([0, 0, 0], dtype=np.float64)
a[0] = 3.2
print(a)

print("****************"*2)
M = np.array([[-1, 2], [0, 4]])
print(M.dtype)
M2 = M.astype(float)  # conversion en float
print(M2)
print(M2.dtype)

print("\n")
M3 = M.astype(bool)  # conversion en bool
print(M3)
print(M3.dtype)



