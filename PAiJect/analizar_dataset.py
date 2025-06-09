import pandas as pd
import numpy as np
from scipy import stats

# SOLUCIÓN TEMPORAL: Usar archivo local
df = pd.read_csv("dataset_cpu.csv")  # Mismo directorio que el script

# 1. Estadísticas básicas (CORRECCIÓN EN LA MODA)
moda_result = stats.mode(df['cpu_percent'])
moda_valor = df['cpu_percent'].mode()[0]

stats_cpu = {
    "Media": df['cpu_percent'].mean(),
    "Mediana": df['cpu_percent'].median(),
    "Moda": moda_valor,
    "Desviación Estándar": df['cpu_percent'].std()
}

print("Estadísticas de Uso de CPU:")
print(f"Media: {stats_cpu['Media']:.2f}")
print(f"Mediana: {stats_cpu['Mediana']:.2f}")
print(f"Moda: {stats_cpu['Moda']}")
print(f"Desviación Estándar: {stats_cpu['Desviación Estándar']:.2f}")

# Matriz de correlación
print("\nMatriz de Correlación:")
print(df.corr())
