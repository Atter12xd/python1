import numpy as np
import random

# Generar secuencias válidas (siguen el patrón alternante)
valid_sequences = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0],  # Permitir pequeñas variaciones
    [1, 0, 1, 0, 0, 1, 0, 1]
]

# Generar secuencias no válidas (aleatorias)
invalid_sequences = [[random.randint(0, 1) for _ in range(8)] for _ in range(4)]

# Combinar ambas listas y crear etiquetas (1 para válidas, 0 para no válidas)
sequences = np.array(valid_sequences + invalid_sequences)
labels = np.array([1] * len(valid_sequences) + [0] * len(invalid_sequences))

print("Secuencias de datos:")
print(sequences)
print("Etiquetas (1=Válida, 0=No válida):")
print(labels)

from sklearn.model_selection import train_test_split

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(sequences, labels, test_size=0.2, random_state=42)

print(f"Entrenamiento: {len(X_train)} secuencias")
print(f"Prueba: {len(X_test)} secuencias")
