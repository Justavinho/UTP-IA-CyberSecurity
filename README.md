# Detección de Ataques DDoS mediante Análisis de Uso de CPU
Este proyecto tiene como objetivo la generación y análisis de un dataset que registra el uso de CPU y procesos activos en un sistema, con el propósito de detectar posibles ataques DDoS (Denegación de Servicio Distribuido).

Contenido del Proyecto
generar_dataset.py: Script para recolectar datos del sistema (uso de CPU y procesos activos) y almacenarlos en un archivo CSV.
dataset_cpu.csv: Dataset generado con las muestras tomadas cada 5 segundos durante 10 minutos.
analizar_dataset.py: Script para análisis estadístico básico del dataset.
analisis_DDoS.py: Script para detectar anomalías y posibles ataques DDoS utilizando técnicas estadísticas.
detection_report.png: Visualización generada automáticamente que muestra el comportamiento del sistema y posibles ataques.

---

Generación del Dataset
El script generar_dataset.py captura los siguientes datos cada 5 segundos durante 10 minutos:

timestamp: Marca temporal UNIX.
cpu_percent: Porcentaje de uso de CPU.
procesos_activos: Número total de procesos activos en el sistema.

Salida: dataset_cpu.csv

---

Análisis Estadístico
El script analizar_dataset.py realiza un análisis exploratorio que incluye:

Media, mediana, moda y desviación estándar del uso de CPU.
Matriz de correlación entre uso de CPU y procesos activos.

---

Detección de Ataques DDoS
El script analisis_DDoS.py implementa un análisis basado en umbrales:

Se calcula un umbral como: media + 3 * desviación estándar.
Se detectan anomalías donde el uso de CPU supera ese umbral.
Se marca como posible ataque DDoS si también hay un número inusualmente alto de procesos activos (> percentil 90).
Se genera un reporte visual en detection_report.png.

---
