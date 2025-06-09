import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Usar datos locales si hay problemas con la URL
df = pd.read_csv("dataset_cpu.csv")

# 1. Convertir timestamp a formato datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df.set_index('timestamp', inplace=True)

# 2. Calcular estadísticas para detección de anomalías
mean_cpu = df['cpu_percent'].mean()
std_cpu = df['cpu_percent'].std()
threshold = mean_cpu + 3 * std_cpu  # Umbral para detección de anomalías

# 3. Detectar posibles ataques DDoS
df['anomalia'] = df['cpu_percent'] > threshold
df['ataque_ddos'] = np.where(
    (df['cpu_percent'] > threshold) &
    (df['procesos_activos'] > df['procesos_activos'].quantile(0.9)),
    "Posible Ataque DDoS",
    "Normal"
)

# 4. Resultados del análisis
anomalias = df[df['anomalia']]
ataques_detectados = df[df['ataque_ddos'] == "Posible Ataque DDoS"]

print("\n----- Detección de Ataques DDoS -----")
print(f"Umbral de detección: {threshold:.2f}% de CPU")
print(f"Total de puntos anómalos: {len(anomalias)}")
print(f"Alertas de posible DDoS: {len(ataques_detectados)}")

if not ataques_detectados.empty:
    print("\n🚨 Eventos de posible ataque detectados:")
    print(ataques_detectados[['cpu_percent', 'procesos_activos']].head())
else:
    print("\n✅ No se detectaron patrones de ataque DDoS")

# 5. Visualización
plt.figure(figsize=(12, 8))

# Gráfico de uso de CPU
plt.subplot(2, 1, 1)
plt.plot(df.index, df['cpu_percent'], label='Uso de CPU (%)', color='blue')
plt.axhline(y=threshold, color='r', linestyle='--', label='Umbral de Ataque')
plt.scatter(anomalias.index, anomalias['cpu_percent'], color='red', label='Anomalías')
plt.title('Monitoreo de Uso de CPU - Detección de DDoS')
plt.ylabel('Uso de CPU (%)')
plt.legend()
plt.grid(True)

# Gráfico de procesos activos
plt.subplot(2, 1, 2)
plt.plot(df.index, df['procesos_activos'], label='Procesos Activos', color='green')
plt.scatter(ataques_detectados.index, ataques_detectados['procesos_activos'],
            color='red', label='Posible DDoS')
plt.title('Procesos Activos en el Sistema')
plt.xlabel('Tiempo')
plt.ylabel('Número de Procesos')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('detection_report.png', dpi=300)
print("\nReporte gráfico guardado como 'detection_report.png'")