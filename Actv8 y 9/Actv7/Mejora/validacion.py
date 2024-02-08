import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "informe": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "fecha": {"type": "string", "format": "date"},
                    "ciudades": {
                        "type": "object",
                        "properties": {
                            "ciudad": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "nombre": {
                                            "type": "string",
                                            "minLength": 1
                                            },
                                        "semestre": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "-numero": {
                                                        "type": "string",
                                                        "minLength": 1
                                                        },
                                                    "CochesVendidos": {
                                                        "type": ["string", "integer"]
                                                        }
                                                },
                                                "required": ["-numero", "CochesVendidos"]
                                            }
                                        }
                                    },
                                    "required": ["nombre", "semestre"]
                                }
                            }
                        },
                        "required": ["ciudad"]
                    }
                },
                "required": ["fecha", "ciudades"]
            }
        }
    },
    "required": ["informe"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "informe": [
        {
            "fecha": "2024-02-01",
            "ciudades": {
                "ciudad": [
                    {
                        "nombre": "Jerez",
                        "semestre": [
                            {
                                "-numero": "1",
                                "CochesVendidos": "120"
                            },
                            {
                                "-numero": "2",
                                "CochesVendidos": "90"
                            }
                        ]
                    },
                    {
                        "nombre": "Cádiz",
                        "semestre": [
                            {
                                "-numero": "1",
                                "CochesVendidos": "200"
                            },
                            {
                                "-numero": "2",
                                "CochesVendidos": "230"
                            }
                        ]
                    },
                    {
                        "nombre": "Sevilla",
                        "semestre": [
                            {
                                "-numero": "1",
                                "CochesVendidos": "190"
                            },
                            {
                                "-numero": "2",
                                "CochesVendidos": "200"
                            }
                        ]
                    }
                ]
            }
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
