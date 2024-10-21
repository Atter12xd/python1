import numpy as np

# Definir dos vectores
u = np.array([2, 3, 5])
v = np.array([1, 0, 4])

# Suma de vectores
suma = u + v
print("Suma de u y v:", suma)

# Resta de vectores
resta = u - v
print("Resta de u y v:", resta)

# Producto punto
producto_punto = np.dot(u, v)
print("Producto punto de u y v:", producto_punto)

# Definir dos matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Suma de matrices
suma_matrices = A + B
print("Suma de matrices A y B:\n", suma_matrices)

# Producto de matrices
producto_matrices = np.dot(A, B)
print("Producto de matrices A y B:\n", producto_matrices)

# Definir la matriz A y el vector b
A = np.array([[2, 1], [1, 3]])
b = np.array([5, 6])

# Resolver el sistema de ecuaciones A x = b
x = np.linalg.solve(A, b)
print("Solución del sistema:\n", x)
