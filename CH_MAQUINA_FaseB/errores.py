from codigo import *

# Como parametro de entrada tiene codigo_ch lista con cada linea del archivo
def verificar_sintaxis(codigo_ch):
    # Elimina elementos que esten las listas
    errores.clear() 
    variables.clear()
    valores_variables.clear()
    tipo_variables.clear()
    etiquetas.clear()
    valores_etiquetas.clear()
    
    item = []
    lin_rev = 1
    # Recorre codigo_ch
    for linea_cod in codigo_ch:
        linea_cod = linea_cod.strip("\n")
        #Guarda cada palabra en la lista item
        item = linea_cod.split(" ")

        #Mientras que en en item exista un vacio
        while("" in item): 
            #Remueve el vacio
            item.remove("")

        #Llama a las funciones dependiendo la palabra que se indique
        if(item[0] == "cargue"): 
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "almacene"):  
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "nueva"):  
            error_funcion_nueva(item, lin_rev)
        elif(item[0] == "lea"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "sume"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "reste"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "multiplique"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "divida"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "potencia"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "modulo"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "concatene"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "elimine"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "extraiga"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "Y"):
            error_funcion_Y_O_NO(item, lin_rev)
        elif(item[0] == "O"):
            error_funcion_Y_O_NO(item, lin_rev)
        elif(item[0] == "NO"):
            error_funcion_Y_O_NO(item, lin_rev)
        elif(item[0] == "muestre"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "imprima"):
            error_funciones_1_operando(item, lin_rev)
        # No obedece a la funcion vaya
        elif(item[0] == "vaya"):
            None
        # No obedece a la funcion vayasi
        elif(item[0] == "vayasi"):
            None
        elif(item[0] == "etiqueta"):
            error_funcion_etiqueta(item, lin_rev)
        elif(item[0] == "retorne"):
            error_retorne(item, lin_rev)
        elif(item[0] == "" or item[0] == " "):
            errores.append("Linea " + str(lin_rev) + ":  " +"Error de identación")
        # No hace nada, comentario no es un error
        elif(es_comentario(item[0]) == True): 
            None 
        else:
            # Si noes ninguno de los errores anteriores, se agraga en errores un error indefinido
            errores.append("Linea " + str(lin_rev) + ":  " +"La función '" + item[0] + "' no ha sido definida")
        item.clear()
        lin_rev +=  1
    
    # Si la memoria sumado con el codido del archivo es mayor al tamaño de la memoria dada es un error 
    # Tamaño arreglo no es suficiente
    if(len(memoria)+len(codigo_ch) > tam_memoria[0]):
        errores.append("CRITICO: MEMORIA INSIFICIENTE")
        


def error_funciones_1_operando(item, lin_rev): 
    # Si item es mayor a 2 es porque hay mas de un operando y es un error
    if(len(item)>2):
        #Agrega error de operando
        errores.append("Linea " + str(lin_rev) + ":  " +"Excede el numero de operaciones/operandos")
    #Lllama a la funcion nombre_var_valido
    elif(nombre_var_valido(item[1]) == False):
        # Si no encuentra las variables validas es un error
        #Lo agrega al arreglo errores
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' No es una variable valida: Error de nombre o nombre reservado")
    # Si en  item esta una variable que no esta en el arreglo variables
    elif(item[1] not in variables):
        #Es un error y se añade al arreglo errores
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' variable no ha sido declarada -> 'nueva nombre_var tipo valor'")

def error_funcion_nueva(item, lin_rev):
    # Tipos de datos que son permitidos
    tipos_de_datos = ["C","I", "R", "L"]
    if(len(item)>4):
        errores.append("Linea " + str(lin_rev) + ":  " +"Excede el numero de operaciones/operandos")
    elif(nombre_var_valido(item[1]) == False):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' nombre de variable NO válido")
    # Si en item no estan los tipos de datos
    elif(item[2] not in tipos_de_datos):
        #Agrega error al arreglo errores
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[2]+ "' Tipo de dato inválido")
    elif(item[2] == "I" and not item[3].isdigit()):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[3]+ "' No pertenece al tipo de dato <"+ item[2] +">  especificado")
    elif(item[2] == "L" and not(item[3] == "1" or item[3] == "0")):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[3]+ "' No pertenece al tipo de dato <"+ item[2] +"> especificado")
    else:
        variables.append(item[1])
        valores_variables.append(item[3])
        tipo_variables.append(item[2])

def error_funcion_Y_O_NO(item, lin_rev): 
    if(len(item)>4): 
        errores.append("Linea " + str(lin_rev) + ":  " +"Excede el numero de operaciones/operandos")
    elif(item[1] not in variables):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' variable no ha sido declarada -> 'nueva nombre_var tipo valor'")
    elif(item[2] not in variables):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[2]+ "' variable no ha sido declarada -> 'nueva nombre_var tipo valor'")
    elif(item[3] not in variables):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[3]+ "' variable no ha sido declarada -> 'nueva nombre_var tipo valor'")

def error_funcion_etiqueta(item, lin_rev):
    if(len(item)>3):
        errores.append("Linea " + str(lin_rev) + ":  " +"Excede el numero de operaciones/operandos")
    elif(nombre_var_valido(item[1]) == False):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' No es una variable valida: Error de nombre o nombre reservado")
    elif(item[1] in variables):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' variable YA ha sido declarada")
    else:
        etiquetas.append(item[1])
        valores_etiquetas.append(item[2])

def error_retorne(item, lin_rev):
    # Si hay mas de un retorne en item
    if(len(item)>2): 
       # Se agrega error 
       errores.append("Linea " + str(lin_rev) + ":  " +"Excede el numero de operaciones/operandos") 

# Arreglo con las funciones que son admitidas en el codigo
def nombre_var_valido(palabra):
    funciones_posibles = ["cargue", "almacene", "nueva", "lea", "sume", "reste", "multiplique", "divida", "potencia", 
        "modulo", "concatene", "elimine", "extraiga", "Y", "O", "NO", "muestre", "imprima", "vaya", "vayasi", "etiqueta", "XXX", "retorne"]
    if(palabra in funciones_posibles):
        return False
    else:
        cadena = ""
        cadena = palabra
        cadena = cadena[0: 1]
        
        if(cadena.isdigit()):
            return False
    return True

def es_comentario(palabra): 
    cadena = ""
    cadena = palabra
    cadena = cadena[0: 2]
    return (cadena == "//") 

# Palabra la retorna como un numero
def es_numero(palabra): 
    return (palabra.isdigit())
