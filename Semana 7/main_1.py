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