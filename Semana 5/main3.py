import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="biblioteca"
)

mycursor = mydb.cursor()

sql = "DELETE FROM libros WHERE anio_publicacion < 2000"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "libros eliminados.")