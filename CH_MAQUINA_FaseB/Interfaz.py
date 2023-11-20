from tkinter import *
from tkinter import ttk 
import tkinter as tk 
from tkinter import filedialog
import ntpath
from codigo import *
from errores import *
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
import time


# Como parametros de entrada tiene el tamaño de kernel y memoria que el usuario ingreso y la ventana del kernel
def validarDatos(tam_ker, tam_mem, una_ventana):
    if(tam_ker > 0 and tam_mem > 0 and tam_mem <= 9999 and tam_ker < tam_mem):
        # mensaje_pre_v.config(text = "Datos correctos")
        #Cierra la ventana
        una_ventana.destroy()
        datos_ker_mem(tam_ker, tam_mem)
        #Abre ventana principal

    else:
        #Si no cumple las condiciones muestra el mensaje 
        mensaje_pre_v.config(text = "Datos inválidos, Prueba de nuevo")
        #Borra de la caja de texto los valores
        input_ker.delete(0, tk.END)
        input_mem.delete(0, tk.END)



def abrirArchivo():
    # Se crean variables para manejar mejor los archivos
    global archivoch    
    global codigo_ch

    #En archivoch se guardara la direccion del archivo
    archivoch = filedialog.askopenfilename(initialdir="/CH_MAQUINA/ch", title="Abrir archivo CH", 
        #Flitypes para especificar el tipo de archivo que se admite en este caso .ch
        filetypes = (("Archivos CH", "*.ch"), ("Todo tipo de archivos", "*.*")))
    
    # Si archivoch no esta vacio
    if archivoch != "":  
        #Abre el archivo 
        archivo = open(archivoch, 'r')   
        print("archivo leido correctamente")
        #Imprime el nombre dl archivo en la interfaz
        nomArch.configure(text = "Programa: " + str(ntpath.basename(archivoch)))
        
        #Readlines devuelve una lista con cada linea del archivo, lo guarda en codigo_ch
        codigo_ch = archivo.readlines()
        archivo.close()

        # Recorre la lista con las lineas del archivo
        for i in range(0, len(codigo_ch)):
            #Cada linea la inserta en la tabla
            tablaCod.insert("", 'end',text = "          " + str(i+1), values=(codigo_ch[i],))

    todosCH.append(codigo_ch)
    print('TODOS CH: ', todosCH)


#funcion para boton MOSTRAR MEMORIA
def mostrar_memoria():
    tabla_memoria.delete(*tabla_memoria.get_children())
    actualizar_memoria(memoria)
    for j in range(0, len(memoria)):
        tabla_memoria.insert("", 'end',text =str(j), values=(memoria[j],))


def Compilar(memoria): 
    #llama la funcion verificar sintaxis 
    verificar_sintaxis(codigo_ch)
    # Si no tiene errores
    if(len(errores) == 0):
        # Guarda en memoria el archivo
        memoria += codigo_ch
        #Crea una ventana donde se confirma que no hay errores
        ventana_errores = Tk()
        ventana_errores.geometry("200x200")
        msj_error = Label(ventana_errores, text  = "No se encontraron errores", )
        msj_error.place(x = 50, y = 50)
        btn_error = Button(ventana_errores, text = " CONTINUAR ", command = lambda: ventana_errores.destroy())
        btn_error.place(x = 50, y = 100)
        
        #Lllama la funcion para mostrar memoria 
        # mostrar_memoria()
        ventana_errores.mainloop()

    else:
        # Si hay errores crea una ventana
        ventana_errores = Tk()
        ventana_errores.title('Errores')
        ventana_errores.geometry("520x520")
        msj_error = Label(ventana_errores, text  = "LISTA DE ERRORES")
        msj_error.place(x = 208, y = 20)

        # Se mostrara una tabla con los errores
        tabla_error = ttk.Treeview(ventana_errores, columns = (), height = 20)

        tabla_error.place(x = 20, y =60)
        tabla_error.heading("#0", text  = "Lista de errores")
        tabla_error.column("#0",minwidth=480, width = 480, stretch=NO)
        
        #Recorre errores para insertarlos en la tabla
        for j in range(0, len(errores)):
            tabla_error.insert("", 'end',text = errores[j])
        ventana_errores.mainloop()



def ejecutar(memoria):
    if(len(errores) == 0):
        ejecutar_codigo_ch(codigo_ch)
        nom = str(ntpath.basename(archivoch))
        for j in range(0, len(variables)):
            tabla_var.insert("", 'end', text = "   "+str(1), values=(variables[j], valores_variables[j]))
        #   tabla_memoria.insert("", 'end',text =str(j), values=(variables[j],))

        # for varible in variables():
        #     tabla_var.insert("", 'end', text = "   "+str(1), values=(varible, "95"))





#KERNEL

# Se cre la ventana Memoria donde estaran los datos de memoria y kernel
pre_ventana = Tk()
pre_ventana.title("MEMORIA")
pre_ventana.geometry("300x260")
pre_ventana.resizable(False, False)


tker = IntVar()
tmem = IntVar()

#Texto para indicar que se ingrese el Kernel
input_ker_lab= Label(pre_ventana, text="Kernel", font=('Calibri', 12,'bold'))
input_ker_lab.place(x=60, y=30)

#Texto para indicar que se ingrese el Kernel
input_mem_lab= Label(pre_ventana, text="Memoria", font=('Calibri', 12,'bold'))
input_mem_lab.place(x=60, y=80)

# Cuadro de texto donde el usuario ingresa los datos del Kernel
input_ker = Entry(pre_ventana, textvariable = tker)
input_ker.place(x=140, y=30, width = 110, height = 30)
tker.set(tam_kernel) # 9

# Cuadro de texto donde el usuario ingresa los datos de la memoria
input_mem = Entry(pre_ventana, textvariable = tmem)
input_mem.place(x=140, y=80, width = 110, height = 30)
input_mem.insert(0, 10)

mensaje_pre_v = Label(pre_ventana, text = "Datos por defecto")
mensaje_pre_v.place(x=90, y=115)


#Botones para comprobar los datos ingresados por el usuario
boton_comprobar = Button(pre_ventana, text =" ACEPTAR ", command = lambda: validarDatos(int(tker.get()), int(tmem.get()),pre_ventana))
boton_comprobar.place(x = 100, y = 150)

pre_ventana.mainloop()





# PRINCIPAL

#Se crea la ventana principal, con sus dimensiones y nombre
ventana = Tk()
ventana.title("CH- MAQUINA")
dimx = 1400
dimy = 800
#ventana.geometry(str(dimx) + "x" + str(dimy))
color = 'light grey'

# La ventana se divira princpalmente en 3 secciones 
frame1 = Frame(ventana, bg =color)
frame1.config(width = dimx/3, height = dimy)
frame1.grid(row = 0, column = 0, columnspan = 2, sticky = 'nsew')

# En este frame se encontraran los botoes
framebotones = Frame(frame1, bg = color)
framebotones.config(width = dimx/2, height = 100)
framebotones.grid(row = 0, column = 0, sticky = 'nsew')

#  Esta es una seccion del frame1
frametabla1 = Frame(frame1, bg = color)
frametabla1.config(width = dimx/2, height =450)
frametabla1.grid(row = 1, column = 0, sticky = 'nsew')

# Lugar de tabla
tablaInt = Frame(frametabla1, bg = color)
tablaInt.config(width = dimx/4, height = 450)
tablaInt.grid(row = 0, column = 0, sticky = 'nsew')

# La segunda seccion del frame1
frametabla2 = Frame(frametabla1, bg = color)
frametabla2.config(width = dimx/4, height = 450/2)
frametabla2.grid(row = 0, column = 1, sticky = 'nsew')

# Lugar de tabla
tablaVar = Frame(frametabla2, bg = color)
tablaVar.config(width = dimx/4, height = 450/2)
tablaVar.grid(row = 0, column = 0, sticky = 'nsew')

# Lugar de tabla
TablaEt = Frame(tablaVar, bg = color)
TablaEt.config(width = dimx/4, height = 450/2)
TablaEt.grid(row = 1, column = 0, sticky = 'nsew')

# Segunda seccion de la ventana
frame2 = Frame(ventana, bg = color)
frame2.config(width = dimx/2, height = dimy)
frame2.grid(row = 0, column = 2, sticky = 'nsew')

#Ubicacion de las imagenes
FrameImag = Frame(frame2, bg = color)
FrameImag.config(width = dimx/4, height = dimy)
FrameImag.grid(row = 0, column = 0, sticky = 'nsew')

#Seccion de frame2
frametabla3 = Frame(frame2, bg = color)
frametabla3.config(width = dimx/4, height = dimy)
frametabla3.grid(row = 0, column = 1, sticky = 'nsew')

frame13 = Frame(frame1, bg = color)
frame13.config(width = dimx/2, height =120)
frame13.grid(row = 2, column = 0, sticky = 'nsew')

# lUgar de tabla
TablaMem = Frame(frametabla3,bg = color)
TablaMem.config(width = dimx/4, height = 650)
TablaMem.grid(row = 0, column = 0, sticky = 'nsew')


# Botones de menu 
opciones = Entry(framebotones)
# Boton que llama la funcion abrirArchivo
btAbrir = ttk.Button(framebotones, text="Abrir archivo",  command = lambda: abrirArchivo()).grid(column=1, row=1,pady=15,padx=10 )
# Boton que llama la funcion compilar
btComp = ttk.Button(framebotones, text="Compilar", command = lambda: Compilar(memoria)).grid(column=2, row=1 )
btEje = ttk.Button(framebotones, text="Ejecutar",command = lambda: ejecutar(memoria)).grid(column=3, row=1,padx=10 )
#Boton que llama la funcion mostrar_memoria
btMemoria = ttk.Button(framebotones, text="Memoria", command = lambda: mostrar_memoria()).grid(column=4, row=1 )

#nombre del programa .ch 
nomArch = Label(framebotones, font=('Arial', 10,'bold'))
nomArch.grid(column = 1, row= 2, padx=10)


# Tabla Programa
tablaInt.grid(padx=10, pady=15) 
tablaCod = ttk.Treeview(tablaInt, columns = ("#0"), height = 20)

tablaCod.grid(row=0, column=1,)
tablaCod.heading("#0", text  = "Lineas")
tablaCod.heading("#1", text  = "Instrucción")
tablaCod.column("#0",minwidth=100, width = 100)
tablaCod.column("#1",minwidth=190, width = 190)


# Tabla Variables
tablaVar.grid(padx=10, pady=15)
style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0)
style.configure("mystyle.Treeview.Heading")

tabla_var = ttk.Treeview(tablaVar, columns = ("#0", "#1"), height = 9, style = "mystyle.Treeview")

tabla_var.grid(row=0, column=0, columnspan = 2)
tabla_var.heading("#0", text  = "Pos")
tabla_var.heading("#1", text  = "Variable")
tabla_var.heading("#2", text  = "Valor")

tabla_var.column("#0",minwidth=96, width = 96)
tabla_var.column("#1",minwidth=96, width = 96)
tabla_var.column("#2",minwidth=96, width = 96)

#Tabla Etiquetas
TablaEt.grid(padx=10, pady=15)
tabla_eti = ttk.Treeview(TablaEt, columns = ("#0", "#1"), height = 9)

tabla_eti.grid(row=0, column=0)
tabla_eti.heading("#0", text  = "Pos")
tabla_eti.heading("#1", text  = "Etiqueta")
tabla_eti.heading("#2", text  = "Valor")

tabla_eti.column("#0",minwidth=96, width = 96, )
tabla_eti.column("#1",minwidth=96, width = 96, )
tabla_eti.column("#2",minwidth=96, width = 96, )

# Imagen
#Abre imagen con la dirrecion
original_imageImp = Image.open("monitor.jpg")
# Le da nuevo tamaño a la imagen
resized_image = original_imageImp.resize((300,300))
imageImp = ImageTk.PhotoImage(resized_image)
#Posiciona la imagen en el Frame
imageImp_label = Label(FrameImag, image=imageImp)
imageImp_label.grid(row=3, column=2, padx=10, pady=10)

# Informacion de kernel y memoria 
#Obtiene los datos de el tamaño de memoria y kernel
tam_ker = tker.get()
tam_mem = tmem.get()
kernel_final_lab = Label(FrameImag, text = "Kernel: " + str(tam_ker),  font= ('Calibri', 12,'bold'))
memoria_final_lab = Label(FrameImag, text = "Memoria: " + str(tam_mem),  font=('Calibri', 12,'bold'))
kernel_final_lab.place(x = 70, y = 400)
memoria_final_lab.place(x = 170, y = 400)

# Tabla Memoria
TablaMem.config(bd = 13) 
TablaMem.grid_propagate(False)
tabla_memoria = ttk.Treeview(TablaMem, columns = ("#0"), height = 35)

tabla_memoria.grid(row=0, column=0, columnspan = 2)
tabla_memoria.heading("#0", text  = "Dirección")
tabla_memoria.heading("#1", text  = "Contenido")

tabla_memoria.column("#0",minwidth=80, width = 80, stretch=NO)
tabla_memoria.column("#1",minwidth=210, width = 210, stretch=NO)

#Tabla Procesos 
frame13.config(bd = 13) 
frame13.grid_propagate(False)
tabla_ancha = ttk.Treeview(frame13, columns = ("#0", "#1", "#2", "#3",'#4'), height = 6)

tabla_ancha.grid(row=0, column=0, columnspan = 1)
tabla_ancha.heading("#0", text  = "ID")
tabla_ancha.heading("#1", text  = "Programa")
tabla_ancha.heading("#2", text  = "#Ins")
tabla_ancha.heading("#3", text  = " RB")
tabla_ancha.heading("#4", text  = " RLC")
tabla_ancha.heading("#5", text  = " RLP")

tabla_ancha.column("#0",minwidth=102, width = 102, stretch=NO)
tabla_ancha.column("#1",minwidth=102, width = 102, stretch=NO)
tabla_ancha.column("#2",minwidth=102, width = 102, stretch=NO)
tabla_ancha.column("#3",minwidth=102, width = 102, stretch=NO)
tabla_ancha.column("#4",minwidth=106, width = 106, stretch=NO)
tabla_ancha.column("#5",minwidth=102, width = 102, stretch=NO)

ventana.mainloop()




