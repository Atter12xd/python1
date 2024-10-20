# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Datos ficticios de precios de casas
data = {
    'Size': [850, 900, 1200, 1500, 1800, 2200, 2500, 2800, 3000, 3300],
    'Price': [95, 110, 130, 160, 185, 220, 250, 270, 300, 330]
}

df = pd.DataFrame(data)

# Definir la variable independiente (X) y la variable dependiente (y)
X = df[['Size']]
y = df['Price']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)  # Aquí se define y_pred

# Evaluar el modelo usando el error cuadrático medio
mse = mean_squared_error(y_test, y_pred)
print(f'Error Cuadrático Medio: {mse:.2f}')

# Graficar la línea de regresión
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')  # Línea de regresión
plt.xlabel('Tamaño de la Casa (en pies cuadrados)')
plt.ylabel('Precio (en miles de dólares)')
plt.title('Regresión Lineal: Precio vs Tamaño de la Casa')
plt.show()

