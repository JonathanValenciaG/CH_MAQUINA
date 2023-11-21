# planificacion.py

class Proceso:
    def __init__(self, nombre, tiempo_ejecucion):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion

def fcfs(planificacion):
    tiempo_total = 0
    for proceso in planificacion:
        print(f"Ejecutando proceso {proceso.nombre} durante {proceso.tiempo_ejecucion} unidades de tiempo")
        tiempo_total += proceso.tiempo_ejecucion

    print(f"Tiempo total de ejecución: {tiempo_total}")
