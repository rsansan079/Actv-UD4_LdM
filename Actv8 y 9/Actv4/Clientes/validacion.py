import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "cliente": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "-codigo": {
                        "type": "string",
                        "minLength": 1
                        },
                    "descCliente": {
                        "type": "string",
                        "minLength": 1
                        },
                    "numero": {
                        "type": "string",
                        "minLength": 1
                        },
                    "vivienda": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "-ID": {
                                    "type": "string", 
                                    "minLength": 1
                                    },
                                "coste": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "resumen": 
                                {"type": "string",
                                 "minLength": 1
                                 },
                                "plazo": {
                                    "type": "string",
                                    "minLength": 1
                                    }
                            },
                            "required": ["-ID", "coste", "resumen", "plazo"]
                        }
                    }
                },
                "required": ["-codigo", "descCliente", "numero", "vivienda"]
            }
        }
    },
    "required": ["cliente"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "cliente": [
        {
            "-codigo": "AAA-112",
            "descCliente": "Insolvente",
            "numero": "10",
            "vivienda": [
                {
                    "-ID": "001",
                    "coste": "100",
                    "resumen": "Producto muy frágil",
                    "plazo": "10"
                },
                {
                    "-ID": "002",
                    "coste": "130",
                    "resumen": "Producto nada frágil",
                    "plazo": "17"
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