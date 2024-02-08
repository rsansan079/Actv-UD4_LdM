import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "coche": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "-codigo": {
                        "type": "string",
                        "minLength": 1
                        },
                    "descCoche": {
                        "type": "string",
                        "minLength": 1
                        },
                    "plazas": {
                        "type": "string",
                        "minLength": 1
                        },
                    "Tipo": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "-ID": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "potencia": {
                                    "type": "string", 
                                    "minLength": 1
                                    },
                                "marca": {
                                    "type": "string", 
                                    "minLength": 1
                                    },
                                "matricula": {
                                    "type": "string", 
                                    "minLength": 1
                                    }
                            },
                            "required": ["-ID", "potencia", "marca", "matricula"]
                        }
                    }
                },
                "required": ["-codigo", "descCoche", "plazas", "Tipo"]
            }
        }
    },
    "required": ["coche"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "coche": [
        {
            "-codigo": "ABC-123",
            "descCoche": "Sedán",
            "plazas": "5",
            "Tipo": [
                {
                    "-ID": "1",
                    "potencia": "150.5",
                    "marca": "Toyota",
                    "matricula": "1234ABC"
                },
                {
                    "-ID": "2",
                    "potencia": "120.3",
                    "marca": "Honda",
                    "matricula": "6789MKL"
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