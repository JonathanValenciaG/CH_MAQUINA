def ejecutar_codigo_ch(codigo_ch, metodo_planificacion, quantum=5, prioridades=None):
    # Resto del código

    if metodo_planificacion == "Round Robin":
        tiempo_actual = 0

        while i < len(codigo_ch) + 1:
            # Resto del código

            if tiempo_actual >= quantum:
                tiempo_actual = 0
                i = (i + 1) % len(codigo_ch)
            else:
                tiempo_actual += 1
                i += 1

    elif metodo_planificacion == "Round Robin con prioridades":
        prioridades = obtener_prioridades()  # Función para obtener las prioridades de los procesos
        tiempo_actual = 0

        while i < len(codigo_ch) + 1:
            # Resto del código

            proceso_actual = codigo_ch[i - 1]
            if prioridades[proceso_actual] > 0:  # Reemplazar 0 por la prioridad mínima permitida
                tiempo_actual = 0
                i = (i + 1) % len(codigo_ch)
            else:
                tiempo_actual += 1
                i += 1

    elif metodo_planificacion == "SJF expropiativo" or metodo_planificacion == "SJF no expropiativo":
        procesos = obtener_tiempos_de_ejecucion()  # Función para obtener los tiempos de ejecución de los procesos
        tiempo_actual = 0

        while i < len(codigo_ch) + 1:
            # Resto del código

            proceso_actual = codigo_ch[i - 1]
            if metodo_planificacion == "SJF expropiativo":
                procesos.sort()  # Ordenar por tiempo de ejecución si es expropiativo
            if proceso_actual in procesos:
                tiempo_actual += procesos[proceso_actual]
                i += 1
            else:
                i += 1

    elif metodo_planificacion == "FCFS":
        tiempo_actual = 0

        while i < len(codigo_ch) + 1:
            # Resto del código

            tiempo_actual += 1
            i += 1

    elif metodo_planificacion == "Por prioridad expropiativo" or metodo_planificacion == "Por prioridad no expropiativo":
        prioridades = obtener_prioridades()  # Función para obtener las prioridades de los procesos
        tiempo_actual = 0

        while i < len(codigo_ch) + 1:
            # Resto del código

            proceso_actual = codigo_ch[i - 1]
            if proceso_actual in procesos:
                if metodo_planificacion == "Por prioridad expropiativo":
                    prioridades.sort(reverse=True)  # Ordenar por prioridad de manera expropiativa
                tiempo_actual += prioridades[proceso_actual]
                i += 1
            else:
                i += 1

    # Resto del código

