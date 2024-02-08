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
                    "regiones": {
                        "type": "object",
                        "properties": {
                            "region": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "nombre": {
                                            "type": "string",
                                            "minLength": 1
                                            },
                                        "trimestre": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "-numero": {
                                                        "type": "string",
                                                        "minLength": 1
                                                        },
                                                    "librosVendidos": {
                                                        "type": ["string", "integer"]
                                                        }
                                                },
                                                "required": ["-numero", "librosVendidos"]
                                            }
                                        }
                                    },
                                    "required": ["nombre", "trimestre"]
                                }
                            }
                        },
                        "required": ["region"]
                    }
                },
                "required": ["fecha", "regiones"]
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
            "regiones": {
                "region": [
                    {
                        "nombre": "Norte",
                        "trimestre": [
                            {
                                "-numero": "1",
                                "librosVendidos": "24000"
                            },
                            {
                                "-numero": "2",
                                "librosVendidos": "38600"
                            },
                            {
                                "-numero": "3",
                                "librosVendidos": "NO_INFO"
                            },
                            {
                                "-numero": "4",
                                "librosVendidos": "NO_INFO"
                            }
                        ]
                    },
                    {
                        "nombre": "Centro",
                        "trimestre": [
                            {
                                "-numero": "1",
                                "librosVendidos": "NO_INFO"
                            },
                            {
                                "-numero": "2",
                                "librosVendidos": "16080"
                            },
                            {
                                "-numero": "3",
                                "librosVendidos": "25000"
                            },
                            {
                                "-numero": "4",
                                "librosVendidos": "29000"
                            }
                        ]
                    },
                    {
                        "nombre": "sur",
                        "trimestre": [
                            {
                                "-numero": "1",
                                "librosVendidos": "27000"
                            },
                            {
                                "-numero": "2",
                                "librosVendidos": "31400"
                            },
                            {
                                "-numero": "3",
                                "librosVendidos": "40100"
                            },
                            {
                                "-numero": "4",
                                "librosVendidos": "30000"
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
