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

# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunos procesos
    proceso1 = Proceso("P1", 5)
    proceso2 = Proceso("P2", 3)
    proceso3 = Proceso("P3", 8)

    # Lista de procesos en el orden en que llegan
    planificacion_fcfs = [proceso1, proceso2, proceso3]

    # Aplicar el algoritmo FCFS a la lista de procesos
    fcfs(planificacion_fcfs)
