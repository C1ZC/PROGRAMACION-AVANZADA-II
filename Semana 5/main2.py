import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="biblioteca"
)

mycursor = mydb.cursor()

# Crear tabla libros
#mycursor.execute("CREATE TABLE libros (id INT AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(255), codigo VARCHAR(255), anio_publicacion INT, autor VARCHAR(255), editorial VARCHAR(255))")

# Insertar 10 libros 
sql = "INSERT INTO libros (titulo, codigo, anio_publicacion, autor, editorial) VALUES (%s, %s, %s, %s, %s)"
val = [
  ("El principito", "123456", 1943, "Antoine de Saint-Exupéry", "Gallimard"),
  ("Cien años de soledad", "234567", 1967, "Gabriel García Márquez", "Sudamericana"),
  ("La casa de los espíritus", "345678", 1982, "Isabel Allende", "Plaza & Janés"),
  ("El amor en los tiempos del cólera", "456789", 1985, "Gabriel García Márquez", "Oveja Negra"),
  ("Rayuela", "567890", 1963, "Julio Cortázar", "Sudamericana"),
  ("El túnel", "678901", 1948, "Ernesto Sabato", "Losada"),
  ("Don Quijote de la Mancha", "789012", 1605, "Miguel de Cervantes", "Francisco de Robles"),
  ("La metamorfosis", "890123", 1915, "Franz Kafka", "Kurt Wolff Verlag"),
  ("1984", "901234", 1949, "George Orwell", "Secker & Warburg"),
  ("Fahrenheit 451", "012345", 1953, "Ray Bradbury", "Ballantine Books")
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "libros insertados.")