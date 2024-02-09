import tkinter as tk
import mysql.connector
from conexion import actualizar_presentacion_farmaco, eliminar_farmaco

def mostrar_datos(cargar_datos):
    # Establecer la conexión con la base de datos
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="farmacia"
    )

    # Crear un cursor para ejecutar consultas SQL
    cursor = mydb.cursor()

    # Ejecutar una consulta para obtener los datos de los fármacos
    cursor.execute("SELECT * FROM farmacos")

    # Obtener todos los resultados de la consulta
    resultados = cursor.fetchall()

    # Crear una ventana para mostrar los datos
    ventana = tk.Tk()

    def eliminar_farmaco_db(farmaco_id):
        # Eliminar el fármaco de la base de datos
        eliminar_farmaco(farmaco_id)

        # Cerrar la ventana de mostrar
        ventana.destroy()

        # Volver a cargar los datos en el formulario principal
        cargar_datos(farmaco=None)

    def actualizar_farmaco_db(farmaco_id):
        # Establecer una nueva conexión con la base de datos
        mydb_update = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="farmacia"
        )

        # Crear un nuevo cursor para ejecutar consultas SQL
        cursor_update = mydb_update.cursor()

        # Obtener los datos del fármaco por su ID
        cursor_update.execute("SELECT * FROM farmacos WHERE id = %s", (farmaco_id,))
        farmaco = cursor_update.fetchone()

        # Cerrar el cursor y la conexión a la base de datos
        cursor_update.close()
        mydb_update.close()

        # Cerrar la ventana de mostrar
        ventana.destroy()

        # Cargar los datos en el formulario principal
        cargar_datos(farmaco)

    # Crear una tabla para mostrar los datos de los fármacos
    tabla = tk.Label(ventana, text="Datos de los fármacos")
    tabla.pack()

    # Mostrar los resultados en la tabla
    for resultado in resultados:
        # Crear un marco para cada fármaco
        marco = tk.Frame(ventana)
        marco.pack()

        # Mostrar los datos del fármaco en etiquetas
        etiqueta = tk.Label(marco, text="Nombre: " + resultado[1] + " | Laboratorio: " + resultado[2] + " | MG: " + str(resultado[3]) + " | Fecha Elaboración: " + str(resultado[4]) + " | Fecha Vencimiento: " + str(resultado[5]) + " | Presentación: " + resultado[6])
        etiqueta.pack(side=tk.LEFT)

        # Botón de Actualizar
        btn_actualizar = tk.Button(marco, text="Actualizar", command=lambda farmaco_id=resultado[0]: actualizar_farmaco_db(farmaco_id))
        btn_actualizar.pack(side=tk.LEFT)

        # Botón de Eliminar
        btn_eliminar = tk.Button(marco, text="Eliminar", command=lambda farmaco_id=resultado[0]: eliminar_farmaco_db(farmaco_id))
        btn_eliminar.pack(side=tk.LEFT)

    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    mydb.close()

    # Ejecutar el bucle principal de la interfaz gráfica
    ventana.mainloop
