import numpy as np

# Paso 1: Crear un array de 20 números aleatorios entre 0 y 100
array = np.random.randint(0, 101, size=20)
print("Array original:\n", array)

# Paso 2: Calcular estadísticas básicas
min_val = np.min(array)
max_val = np.max(array)
mean_val = np.mean(array)
std_val = np.std(array)

print(f"Valor mínimo: {min_val}")
print(f"Valor máximo: {max_val}")
print(f"Media: {mean_val}")
print(f"Desviación estándar: {std_val}")

# Paso 3: Modificar el array
array = array * 2
print("\nArray multiplicado por 2:\n", array)

# Filtrar elementos mayores a 50
filtered_array = array[array > 50]
print("\nElementos mayores a 50:\n", filtered_array)

# Paso 4: Reshape del array a una matriz de 4x5
reshaped_array = array.reshape(4, 5)
print("\nArray reestructurado (4x5):\n", reshaped_array)

# Paso 5: Operaciones con arrays
# Crear otro array de 4x5 con valores del 1 al 20
another_array = np.arange(1, 21).reshape(4, 5)
print("\nOtro array (4x5):\n", another_array)

# Suma y multiplicación elemento a elemento
sum_arrays = reshaped_array + another_array
mult_arrays = reshaped_array * another_array

print("\nSuma de los arrays:\n", sum_arrays)
print("\nMultiplicación de los arrays:\n", mult_arrays)