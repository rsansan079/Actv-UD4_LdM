import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
    "teléfono": {
    "type": "string",
    "minimum": 1
    },
    "fecha": {
    "type": "string",
    "minimum": 1
    },
    "hora": {
    "type": "string",
    "minimum": 1
    },
    "mensaje": {
        "type": "string",
        "minimum": 1
    }
   }
}

# Archivo JSON a validar
archivo_json = '''
{
                    "telefono": "955 55 66 55",
                    "fecha": "1/7/2011",
                    "hora": "23:55",
                    "mensaje": "Juegol: Tetris"
                },
                {
                    "telefono": "745 15 56 11",
                    "fecha": "22/9/2011",
                    "hora": "15:05",
                    "mensaje": "Juego2: Arkanoid"
                },
                {
                    "telefono": "842 35 22 00",
                    "fecha": "10/11/2011",
                    "hora": "09:22",
                    "mensaje": "Juego3: Comecocos"
                }
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.