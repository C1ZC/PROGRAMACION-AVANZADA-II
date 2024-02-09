import matplotlib.pyplot as plt
import numpy as np

# Datos de la tabla
escalafon = ['Instructor', 'Asistente', 'Agregado', 'Asociado']
casos = [945, 698, 736, 590]

# Gráfico de barras
plt.bar(escalafon, casos)
plt.title('Clasificación de profesores según su escalafón')
plt.xlabel('Escalafón')
plt.ylabel('Casos')
plt.show()

# Generar Series 1, 2 y 3
media1 = 750
varianza1 = 50
registros1 = 700

media2 = 900
varianza2 = 20
registros2 = 700

media3 = 500
varianza3 = 40
registros3 = 700

serie1 = np.random.normal(media1, varianza1, registros1)
serie2 = np.random.normal(media2, varianza2, registros2)
serie3 = np.random.normal(media3, varianza3, registros3)

# Gráficos Boxplot de las Series 1, 2 y 3
plt.boxplot([serie1, serie2, serie3])
plt.xticks([1, 2, 3], ['Serie 1', 'Serie 2', 'Serie 3'])
plt.title('Gráfico Boxplot de las Series 1, 2 y 3')
plt.show()

