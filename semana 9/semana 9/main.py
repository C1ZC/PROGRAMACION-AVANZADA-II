import tkinter as tk
from farmacos import Farmaco
from conexion import insertar_farmaco
from mostrar import mostrar_datos

def borrar_campos():
    entry_nombre.delete(0, tk.END)
    entry_laboratorio.delete(0, tk.END)
    entry_mg.delete(0, tk.END)
    entry_fecha_elaboracion.delete(0, tk.END)
    entry_fecha_vencimiento.delete(0, tk.END)
    entry_presentacion.delete(0, tk.END)

def cargar_datos(farmaco):
    entry_nombre.delete(0, tk.END)
    entry_laboratorio.delete(0, tk.END)
    entry_mg.delete(0, tk.END)
    entry_fecha_elaboracion.delete(0, tk.END)
    entry_fecha_vencimiento.delete(0, tk.END)
    entry_presentacion.delete(0, tk.END)

#los campos de entrada se borrarán sin intentar realizar ninguna operacion
    if farmaco is not None:
        entry_nombre.insert(tk.END, farmaco[1])
        entry_laboratorio.insert(tk.END, farmaco[2])
        entry_mg.insert(tk.END, str(farmaco[3]))
        entry_fecha_elaboracion.insert(tk.END, str(farmaco[4]))
        entry_fecha_vencimiento.insert(tk.END, str(farmaco[5]))
        entry_presentacion.insert(tk.END, farmaco[6])

def insertar():
    # Obtener los valores del formulario
    nombre = entry_nombre.get()
    laboratorio = entry_laboratorio.get()
    mg = entry_mg.get()
    fecha_elaboracion = entry_fecha_elaboracion.get()
    fecha_vencimiento = entry_fecha_vencimiento.get()
    presentacion = entry_presentacion.get()

    # Crear un nuevo objeto Farmaco
    farmaco = Farmaco(nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion)

    # Insertar el fármaco en la base de datos
    insertar_farmaco(farmaco)

    # Borrar los campos de entrada
    borrar_campos()

# Crear la ventana principal
root = tk.Tk()

# Crear los campos de entrada (Entry) y etiquetas (Label) del formulario
label_nombre = tk.Label(root, text="Nombre:")
entry_nombre = tk.Entry(root)

label_laboratorio = tk.Label(root, text="Laboratorio:")
entry_laboratorio = tk.Entry(root)

label_mg = tk.Label(root, text="MG:")
entry_mg = tk.Entry(root)

label_fecha_elaboracion = tk.Label(root, text="Fecha de Elaboración:")
entry_fecha_elaboracion = tk.Entry(root)

label_fecha_vencimiento = tk.Label(root, text="Fecha de Vencimiento:")
entry_fecha_vencimiento = tk.Entry(root)

label_presentacion = tk.Label(root, text="Presentación:")
entry_presentacion = tk.Entry(root)

# Crear los botones para realizar las operaciones
btn_insertar = tk.Button(root, text="Insertar", command=insertar)
btn_mostrar = tk.Button(root, text="Mostrar Datos", command=lambda: mostrar_datos(cargar_datos))

# Ubicar los elementos en la ventana
label_nombre.pack()
entry_nombre.pack()

label_laboratorio.pack()
entry_laboratorio.pack()

label_mg.pack()
entry_mg.pack()

label_fecha_elaboracion.pack()
entry_fecha_elaboracion.pack()

label_fecha_vencimiento.pack()
entry_fecha_vencimiento.pack()

label_presentacion.pack()
entry_presentacion.pack()

btn_insertar.pack()
btn_mostrar.pack()

# Iniciar el bucle principal de la aplicación
root.mainloop()