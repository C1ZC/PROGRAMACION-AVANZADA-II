import pandas as pd

def generar_registro():
    # Crear un diccionario con los datos de los médicos
    data = {
        'nombre': ['Juan', 'Pedro', 'María', 'Ana'],
        'apellido': ['Pérez', 'García', 'López', 'González'],
        'RUT': ['11.111.111-1', '22.222.222-2', '33.333.333-3', '44.444.444-4'],
        'sexo': ['M', 'M', 'F', 'F'],
        'direccion': ['Calle 1', 'Calle 2', 'Calle 3', 'Calle 4'],
        'edad': [35, 42, 27, 31]
    }
    
    # Crear un DataFrame a partir del diccionario
    df = pd.DataFrame(data)
    
    return df