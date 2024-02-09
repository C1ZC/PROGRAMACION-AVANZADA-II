import tkinter as tk
root = tk.Tk()
# Crear una ventana
ventana = tk.Tk()
ventana.title("Encuesta")

# Crear un contenedor para el formulario
formulario = tk.Frame(ventana)
formulario.pack(padx=20, pady=20)

# Agregar etiquetas y campos de entrada de texto
tk.Label(formulario, text="Nombre:").grid(row=0, column=0, sticky="w")
entrada_nombre = tk.Entry(formulario)
entrada_nombre.grid(row=0, column=1)

tk.Label(formulario, text="Apellido:").grid(row=1, column=0, sticky="w")
entrada_apellido = tk.Entry(formulario)
entrada_apellido.grid(row=1, column=1)

tk.Label(formulario, text="RUT:").grid(row=2, column=0, sticky="w")
entrada_rut = tk.Entry(formulario)
entrada_rut.grid(row=2, column=1)

tk.Label(formulario, text="Teléfono:").grid(row=3, column=0, sticky="w")
entrada_telefono = tk.Entry(formulario)
entrada_telefono.grid(row=3, column=1)

# Agregar un menú desplegable para seleccionar el sexo
tk.Label(formulario, text="Sexo:").grid(row=4, column=0, sticky="w")
opcion_seleccionada = tk.StringVar(value="Masculino")
menu_sexo = tk.OptionMenu(formulario, opcion_seleccionada, "Masculino", "Femenino")
menu_sexo.grid(row=4, column=1, sticky="w")

# Agregar botones de opción para responder la pregunta
tk.Label(formulario, text="¿Está de acuerdo con la construcción de la escuela en su comunidad?").grid(row=5, column=0, sticky="w")
respuesta_seleccionada = tk.StringVar(value="Sí")
opcion_si = tk.Radiobutton(formulario, text="Sí", variable=respuesta_seleccionada, value="Sí")
opcion_si.grid(row=6, column=0, sticky="w")
opcion_no = tk.Radiobutton(formulario, text="No", variable=respuesta_seleccionada, value="No")
opcion_no.grid(row=6, column=1, sticky="w")

# Agregar un botón para enviar el formulario
def enviar_formulario():
    # Obtener los datos ingresados por el usuario
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    rut = entrada_rut.get()
    telefono = entrada_telefono.get()
    sexo = opcion_seleccionada.get()
    respuesta = respuesta_seleccionada.get()
    # Imprimir los datos en la consola
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("RUT:", rut)
    print("Teléfono:", telefono)
    print("Sexo:", sexo)
    print("Respuesta:", respuesta)

boton_enviar = tk.Button(formulario, text="Enviar", command=enviar_formulario)
boton_enviar.grid(row=7, column=1, sticky="e")

# Iniciar el bucle principal de la ventana
ventana.mainloop()
root.mainloop()