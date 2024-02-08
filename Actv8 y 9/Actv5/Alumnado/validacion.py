import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "alumnado": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "alumno": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "NIF": {
                                    "type": "string", 
                                    "minLength": 1
                                    },
                                "Resultado": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "Observaciones": {
                                    "type": "string"
                                    },
                                "IP": {
                                    "type": "string",
                                    "minLength": 1
                                    }
                            },
                            "required": ["NIF", "Resultado", "IP"]
                        }
                    }
                },
                "required": ["alumno"]
            }
        }
    },
    "required": ["alumnado"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "alumnado": [
        {
            "alumno": [
                {
                    "NIF": "123456789A",
                    "Resultado": "apto",
                    "Observaciones": "Alumno bueno en programación.",
                    "IP": "192.168.1.2"
                },
                {
                    "NIF": "987654321B",
                    "Resultado": "No apto",
                    "IP": "00:1A:2B:3C:4D:5E"
                }
            ]
        }
    ]
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación. 