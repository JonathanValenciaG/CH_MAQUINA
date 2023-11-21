import tkinter as tk

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

def mostrar_select():
    # Crear una ventana principal
    ventana = tk.Tk()
    ventana.title("Selección")
    ventana.geometry("200x300")

    # Función para manejar el botón de selección
    def seleccionar_opcion():
        seleccion = var.get()
        if seleccion == 4:  # FCFS seleccionado
            # Crear algunos procesos
            proceso1 = Proceso("P1", 5)
            proceso2 = Proceso("P2", 3)
            proceso3 = Proceso("P3", 8)

            # Lista de procesos en el orden en que llegan
            planificacion_fcfs = [proceso1, proceso2, proceso3]

            # Aplicar el algoritmo FCFS a la lista de procesos
            fcfs(planificacion_fcfs)

        # Puedes agregar más condiciones para otros algoritmos aquí

        ventana.destroy()

    # Crear una variable de tipo IntVar para almacenar la selección
    var = tk.IntVar()

    # Crear botones de selección
    opcion1 = tk.Radiobutton(ventana, text="RR", variable=var, value=1)
    opcion2 = tk.Radiobutton(ventana, text="SJF Expropiativo", variable=var, value=2)
    opcion3 = tk.Radiobutton(ventana, text="SJF No Expropiativo", variable=var, value=3)
    opcion4 = tk.Radiobutton(ventana, text="FCFS", variable=var, value=4)
    opcion5 = tk.Radiobutton(ventana, text="Prioridad", variable=var, value=5)

    # Crear un botón para confirmar la selección
    boton_confirmar = tk.Button(ventana, text="Confirmar", command=seleccionar_opcion)

    # Organizar los elementos usando grid para centrarlos
    opcion1.grid(row=0, column=0, pady=5, sticky="w")
    opcion2.grid(row=1, column=0, pady=5, sticky="w")
    opcion3.grid(row=2, column=0, pady=5, sticky="w")
    opcion4.grid(row=3, column=0, pady=5, sticky="w")
    opcion5.grid(row=4, column=0, pady=5, sticky="w")
    boton_confirmar.grid(row=5, column=0, pady=10)

    # Iniciar el bucle de la interfaz gráfica
    ventana.mainloop()

# Llamar a la función para mostrar la ventana de selección
mostrar_select()
