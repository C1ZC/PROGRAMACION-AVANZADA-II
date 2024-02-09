from registro import generar_registro
import pandas as pd

# Generar el registro de médicos
registro = generar_registro()

# Dividir el registro en dos subconjuntos según el sexo
registro_masculino = registro[registro['sexo'] == 'M']
registro_femenino = registro[registro['sexo'] == 'F']

# Concatenar los dos subconjuntos en un solo conjunto
registro_total = pd.concat([registro_masculino, registro_femenino])

# Imprimir el registro completo
print(registro)

# Imprimir el registro de médicos masculinos
print(registro_masculino)

# Imprimir el registro de médicos femeninos
print(registro_femenino)

# Imprimir el registro completo consolidado
print(registro_total)