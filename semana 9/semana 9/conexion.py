import mysql.connector
from farmacos import Farmaco

# Establecer la conexión con la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="farmacia"
)

# Función para insertar un nuevo fármaco en la base de datos
def insertar_farmaco(farmaco):
    cursor = mydb.cursor()
    sql = "INSERT INTO farmacos (nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (farmaco.nombre, farmaco.laboratorio, farmaco.mg, farmaco.fecha_elaboracion, farmaco.fecha_vencimiento, farmaco.presentacion)
    cursor.execute(sql, valores)
    mydb.commit()
    print("Fármaco insertado correctamente.")

# Función para eliminar un fármaco de la base de datos por su ID
def eliminar_farmaco(farmaco):
    cursor = mydb.cursor()
    sql = "DELETE FROM farmacos WHERE id = %s"
    valores = (farmaco,)
    cursor.execute(sql, valores)
    mydb.commit()
    print("Fármaco eliminado correctamente.")


# Función para actualizar la presentación de un fármaco en la base de datos por su nombre
def actualizar_presentacion_farmaco(nombre, nueva_presentacion):
    cursor = mydb.cursor()
    sql = "UPDATE farmacos SET presentacion = %s WHERE nombre = %s"
    valores = (nueva_presentacion, nombre)
    cursor.execute(sql, valores)
    mydb.commit()
    print("Presentación de fármaco actualizada correctamente.")
