import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="biblioteca"
)

mycursor = mydb.cursor()

year = datetime.datetime.now().year

sql = "SELECT * FROM libros WHERE anio_publicacion = %s"
val = (year, )

mycursor.execute(sql, val)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)