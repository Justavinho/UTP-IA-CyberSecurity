import psutil
import csv
import time

# Configuración
TIEMPO_TOTAL = 600  # 10 minutos en segundos
INTERVALO = 5  # Muestras cada 5 segundos
ARCHIVO = "dataset_cpu.csv"

# Crear archivo CSV
with open(ARCHIVO, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "cpu_percent", "procesos_activos"])

    start_time = time.time()
    while (time.time() - start_time) < TIEMPO_TOTAL:
        # Obtener datos
        timestamp = int(time.time())
        cpu_uso = psutil.cpu_percent(interval=1)
        procesos = len(psutil.pids())

        # Escribir fila
        writer.writerow([timestamp, cpu_uso, procesos])
        time.sleep(INTERVALO)