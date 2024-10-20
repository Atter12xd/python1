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

# Mostrar los primeros 5 registros
print(df.head())