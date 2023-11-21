import random
from queue import PriorityQueue

codigo_ch = []  #archivo.ch guardado en una lista
memoria = []  #lista memoria
errores = []  #lista de errores
variables = [] # Lista de variables
valores_variables = []
tipo_variables = []
posicion_varibles = []
etiquetas = []
valores_etiquetas = []
quantum = 5
proces = []

todosCH = []


#Texto para las imagenes
texto_monitor = [] 
texto_impresora = []

acumulador = [0]  #solo es un valor acumulador[0]

tam_kernel = 9 # 10*z+9 , z =0
tam_memoria = [100]  


def datos_ker_mem(tam_ker, tam_mem):
    #Si cambian los tamaños del kernel y memoria los actualiza
    tam_kernel =int(tam_ker)
    tam_memoria[0] =int(tam_mem)

    #Actualiza la memoria con el tamaño del kernel 
    ker = tam_kernel+1
    tam_ker = ['KERNEL']*ker
    memoria.extend(tam_ker)
    # print("ASIGNAMOS y ahora tam_memoria y tam_mem son", tam_memoria, " y " , tam_kernel)


def ejecutar_codigo_ch(codigo_ch):
    # print("VARIABLES: ", variables)
    # print("VALORES VARIABLES: ", valores_variables)
    # print("POSICION VARIABLES: ", posicion_varibles)
    # print("llegamos con acumulador[0]", acumulador)
    # print()
    item = []
    texto_monitor.clear()
    texto_impresora.clear()

    #for linea_cod in codigo_ch:
    i = 1
    
    while(i < len(codigo_ch) + 1):
        linea_cod = codigo_ch[i - 1]
        linea_cod = linea_cod.strip("\n")
        item = linea_cod.split(" ")
        while("" in item): 
            item.remove("")

        print("vamos en la linea: ", i , " --->: ", item)
        
        
        if(item[0] == "cargue"): # ok 
            acumulador[0] = funcion_cargue(item)
            i+=1
       
        
            print("cargue: cargamos variable y ahora acumulador[0] vale: ", acumulador)
        elif(item[0] == "almacene"): # ok 
            funcion_almacene(item, acumulador)
            i+=1 
          
            print("almacene: actualizamos variables ", valores_variables)
        elif(item[0] == "nueva"): #las variables ya se han creado 
            i+=1
            None                            
        elif(item[0] == "lea"): # ??? 
            i+=1
          
            None                            
        elif(item[0] == "sume"): # ok
            acumulador[0] = funcion_sume(item, acumulador)
            i+=1
           
            print("sume: sumamos y ahora cumulador vale: ", acumulador)
        elif(item[0] == "reste"):
            acumulador[0] = funcion_reste(item, acumulador)
            i+=1
          
            print("reste: restamos y ahora acumulador[0] vale: ", acumulador)
        elif(item[0] == "multiplique"):
            acumulador[0] = funcion_multiplique(item, acumulador)
            i+=1
           
            print("multiplique: multiplicamos y ahora acumulador[0] vale: ", acumulador)
        elif(item[0] == "divida"):
            acumulador[0] = funcion_divida(item, acumulador)
            i+=1
       
            print("divida: dividimos y ahora acumulador[0] vale: ", acumulador)
        elif(item[0] == "potencia"):
            acumulador[0] = funcion_potencia(item, acumulador)
            i+=1
          
            print("potencia: hacemos potencia y ahora acumulador[0] vale: ", acumulador)
        elif(item[0] == "modulo"):
            acumulador[0] = funcion_modulo(item, acumulador)
            i+=1
          
            print("modulo: hacemos modulo y ahora acumulador[0] vale: ", acumulador)
        elif(item[0] == "concatene"):
            i+=1
          
            None
        elif(item[0] == "elimine"):
            i+=1
         
            None
        elif(item[0] == "extraiga"):
            i+=1
    
            None
        elif(item[0] == "Y"):
            i+=1
        
            None
        elif(item[0] == "O"):
            None
        elif(item[0] == "NO"):
            i+=1
          
            None
        elif(item[0] == "muestre"):
            i+=1
      
            palabra = str(consultar_valor_variable(item[1]))
            texto_monitor.append(palabra + " ")
        elif(item[0] == "imprima"):
            i+=1
        
            palabra = str(consultar_valor_variable(item[1]))
            texto_impresora.append(palabra + " ")
        elif(item[0] == "vaya"):
            i = funcion_vaya(item)
            
        elif(item[0] == "vayasi"):
            i = funcion_vayasi(item, acumulador, i)
            
            print("vayasi: vamos a saltar a la linea: ", i)
        elif(item[0] == "etiqueta"):
            i+=1
            None    #las etiquetas ya se han creado
        elif(item[0] == "XXX"):
            i+=1
            None  #falta definir la función
        elif(item[0] == "retorne"):
            i+=1
        else:
            print("ENTRAMOS A ULTIMO ELSE")
            i+=1
        item.clear()
    
    print("LA RESPUESTA ES: ", valores_variables[3])


def consultar_valor_variable(palabra):
    indice = variables.index(palabra)
    

    if(tipo_variables[indice] == "C"):
        return valores_variables[indice]
    elif(tipo_variables[indice] == "I"):
        return int(valores_variables[indice])

def consultar_valor_etiqueta(palabra): 
    indice = etiquetas.index(palabra)
    return int(valores_etiquetas[indice])

def funcion_cargue(item): 
    return consultar_valor_variable(item[1])

def funcion_almacene(item, acumulador):
    indice = variables.index(item[1])
    valores_variables[indice] = acumulador[0]

def funcion_sume(item, acumulador):
    valor = consultar_valor_variable(item[1])
    return (acumulador[0] + valor)

def funcion_reste(item, acumulador):
    valor = consultar_valor_variable(item[1])
    return (acumulador[0] - valor)

def funcion_multiplique(item, acumulador): 
    valor = consultar_valor_variable(item[1])
    return (acumulador[0] * valor)

def funcion_divida(item, acumumulador):
    valor = consultar_valor_variable(item[1])
    return (acumulador[0] / valor)

def funcion_potencia(item, acumumulador):
    valor = consultar_valor_variable(item[1])
    return (acumulador[0] ** valor)

def funcion_modulo(item, acumulador):
    valor = consultar_valor_variable(item[1])
    return (acumulador[0] % valor)


def funcion_vayasi(item, acumulador, i): 
    if(acumulador[0] > 0): 
        return consultar_valor_etiqueta(item[1])
    elif(acumulador[0] < 0):
        return consultar_valor_etiqueta(item[2])
    else:
        return i+1

def funcion_vaya(item): 
    return consultar_valor_etiqueta(item[1])

def actualizar_memoria(memoria): 

    memoria[0] = "ACUMULADOR 🡆 " + str(acumulador[0])
    # valorAcumulador = "ACUMULADOR 🡆 " + str(acumulador[0])
    # memoria.insert(0,valorAcumulador)


