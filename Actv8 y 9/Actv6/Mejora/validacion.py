import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "bach": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "asignatura": {
                        "type": "object",
                        "properties": {
                            "nombre": {
                                "type": "string",
                                       "minLength": 1
                                       },
                            "contenidos": {
                                "type": "object",
                                "properties": {
                                    "unidad": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "-tipo": {
                                                    "type": "string", 
                                                    "minLength": 1
                                                    },
                                                "titulo": {
                                                    "type": "string", 
                                                    "minLength": 1
                                                    },
                                                "descripcion": {
                                                    "type": "string", 
                                                    "minLength": 1
                                                    }
                                            },
                                            "required": ["-tipo", "titulo", "descripcion"]
                                        }
                                    }
                                },
                                "required": ["unidad"]
                            }
                        },
                        "required": ["nombre", "contenidos"]
                    },
                    "modulo": {
                        "type": "object",
                        "properties": {
                            "nombre": {"type": "string", "minLength": 1},
                            "contenidos": {
                                "type": "object",
                                "properties": {
                                    "unidad": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "-tipo": {"type": "string", "minLength": 1},
                                                "titulo": {"type": "string", "minLength": 1},
                                                "descripcion": {"type": "string", "minLength": 1}
                                            },
                                            "required": ["-tipo", "titulo", "descripcion"]
                                        }
                                    }
                                },
                                "required": ["unidad"]
                            }
                        },
                        "required": ["nombre", "contenidos"]
                    }
                },
                "required": ["asignatura", "modulo"]
            }
        }
    },
    "required": ["bach"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "bach": [
        {
            "asignatura": {
                "nombre": "Biología",
                "contenidos": {
                    "unidad": [
                        {
                            "-tipo": "Teórica",
                            "titulo": "1.Célula eucariota y procariota",
                            "descripcion": "Se aprenden todos los componentes de las células y sus funciones"
                        },
                        {
                            "-tipo": "Práctica",
                            "titulo": "Los órganos humanos",
                            "descripcion": "Se hacen prácticas con órganos de cerdo"
                        }
                    ]
                }
            },
            "modulo": {
                "nombre": "Historia",
                "contenidos": {
                    "unidad": [
                        {
                            "-tipo": "Teórica",
                            "titulo": "Tema 1. Guerra civil",
                            "descripcion": "Conocer lo ocurrido en el período de la guerra civil española"
                        },
                        {
                            "-tipo": "Práctica",
                            "titulo": "Lectura La Mula",
                            "descripcion": "Examen práctico de la lectura"
                        }
                    ]
                }
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
