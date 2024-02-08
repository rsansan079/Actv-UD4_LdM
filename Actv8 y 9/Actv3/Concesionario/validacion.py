import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
    "código": {
    "type": "id",
    "minimum": 1
    },
    "marca": {
    "type": "string",
    "minimum": 1
    },
    "modelo": {
    "type": "string",
    "minimum": 1
    },
    "matricula": {
        "type": "string",
        "minimum": 1
    }, 
    "potencia": {
        "type": "string",
        "minimum": 1
    },
     "plazas": {
        "type": "int",
        "minimum": 1
    }, 
     "puertas": {
        "type": "int",
        "minimum": 1
    }
   }
}

# Archivo JSON a validar
archivo_json = '''
{
                    "codigo": "001",
                    "marca": "Ford",
                    "modelo": "Focus",
                    "matricula": "3312HJI",
                    "potencia": "120 cv",
                    "plazas": "5",
                    "puertas": "4"
                },
                {
                    "codigo": "002",
                    "marca": "Merceds",
                    "modelo": "sl 55 amg",
                    "matricula": "2233EXZ",
                    "potencia": "532 cv",
                    "plazas": "2",
                    "puertas": "3"
                }
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.