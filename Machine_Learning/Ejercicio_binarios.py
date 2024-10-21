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


from sklearn.ensemble import RandomForestClassifier

# Crear y entrenar el modelo de Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Hacer predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

# Generar la matriz de confusión y reporte de clasificación
print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

import seaborn as sns
import matplotlib.pyplot as plt

# Mostrar la matriz de confusión de forma gráfica
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="Blues")
plt.xlabel('Predicción')
plt.ylabel('Verdadero')
plt.title('Matriz de Confusión')
plt.show()

# Mostrar la importancia de las características (cada bit)
importances = model.feature_importances_
features = [f'Bit {i+1}' for i in range(8)]
indices = np.argsort(importances)

plt.figure(figsize=(8,6))
plt.title('Importancia de las Características')
plt.barh(range(len(indices)), importances[indices], align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Importancia Relativa')
plt.show()
