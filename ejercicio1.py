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