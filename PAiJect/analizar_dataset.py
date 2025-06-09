import pandas as pd
import numpy as np
from scipy import stats

# Descargar dataset desde GitHub
url = "https://raw.githubusercontent.com/tu_usuario/UTP-IA-Ciberseguridad/main/dataset_cpu.csv"
df = pd.read_csv(url)

# 1. Estadísticas básicas
stats_cpu = {
    "Media": df['cpu_percent'].mean(),
    "Mediana": df['cpu_percent'].median(),
    "Moda": stats.mode(df['cpu_percent'])[0][0],
    "Desviación Estándar": df['cpu_percent'].std()
}

# 2. Matriz de correlación
correlation_matrix = df.corr()

# Mostrar resultados
print("Estadísticas de Uso de CPU:")
for key, value in stats_cpu.items():
    print(f"{key}: {value:.2f}")

print("\nMatriz de Correlación:")
print(correlation_matrix)