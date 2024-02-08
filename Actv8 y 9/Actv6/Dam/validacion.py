import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "cfgs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "modulo": {
                        "type": "array",
                        "items": {
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
                                                    "-tipo": {
                                                        "type": "string",
                                                        "minLength": 1
                                                        },
                                                    "numero": {
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
                                                "required": ["-tipo", "numero", "titulo", "descripcion"]
                                            }
                                        }
                                    },
                                    "required": ["unidad"]
                                }
                            },
                            "required": ["nombre", "contenidos"]
                        }
                    }
                },
                "required": ["modulo"]
            }
        }
    },
    "required": ["cfgs"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "cfgs": [
        {
            "modulo": [
                {
                    "nombre": "Entornos de desarrollo",
                    "contenidos": {
                        "unidad": [
                            {
                                "-tipo": "Teórica",
                                "numero": "1",
                                "titulo": "Lenguajes de programación. Herramientas. Ciclo de desarrollo del software",
                                "descripcion": "Se aprenden la mayoría de tipos de lenguajes de programación que hay y para qué uso son adecuados"
                            },
                            {
                                "-tipo": "Práctica",
                                "numero": "2",
                                "titulo": "IDE. Entornos de desarrollo integrados",
                                "descripcion": "Aplicación de software que ayuda a los programadores a desarrollar"
                            },
                            {
                                "-tipo": "Práctica",
                                "numero": "3",
                                "titulo": "CASE. Ingeniería del software asistida por ordenador",
                                "descripcion": "Uso de software para simular el rendimiento con el objetivo de mejorar los productos"
                            }
                        ]
                    }
                },
                {
                    "nombre": "Base de Datos",
                    "contenidos": {
                        "unidad": [
                            {
                                "-tipo": "Teórica",
                                "numero": "1",
                                "titulo": "Almacenamiento de la información",
                                "descripcion": "Conocer características principales y tipos de ficheros."
                            },
                            {
                                "-tipo": "Práctica",
                                "numero": "2",
                                "titulo": "Bases de Datos Relacionales",
                                "descripcion": "La base de datos relacional (BDR) es un tipo de base de datos (BD) implementada bajo las especificaciones del modelo relacional."
                            }
                        ]
                    }
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


