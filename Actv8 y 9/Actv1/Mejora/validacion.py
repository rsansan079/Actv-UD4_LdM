import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "actores": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "actor": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "nombre": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "apellido1": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "apellido2": {
                                    "type": ["string", "object"],
                                    "minLength": 1
                                    },
                                "fecha_nac": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "edad": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "peliculas": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "oscar": {
                                    "type": "string", 
                                    "minLength": 1
                                    }
                            },
                            "required": ["nombre", "apellido1", "fecha_nac", "edad", "peliculas", "oscar"]
                        }
                    }
                },
                "required": ["actor"]
            }
        }
    },
    "required": ["actores"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "actores": [
        {
            "actor": [
                {
                    "nombre": "Brad",
                    "apellido1": "Pitt",
                    "apellido2": {},
                    "fecha_nac": "18/12/1963",
                    "edad": "60",
                    "peliculas": "Troya",
                    "oscar": "2"
                },
                {
                    "nombre": "Tom",
                    "apellido1": "Ellis",
                    "apellido2": {},
                    "fecha_nac": "17/11/1978",
                    "edad": "45",
                    "peliculas": "Rush",
                    "oscar": "0"
                },
                {
                    "nombre": "Jonathan ",
                    "apellido1": "Bernthal ",
                    "apellido2": {},
                    "fecha_nac": "20/09/1976",
                    "edad": "47",
                    "peliculas": "Fury",
                    "oscar": "0"
                },
                {
                    "nombre": "Christian ",
                    "apellido1": "Bale ",
                    "apellido2": {},
                    "fecha_nac": "30/01/1974",
                    "edad": "49",
                    "peliculas": "American Psycho",
                    "oscar": "1"
                },
                {
                    "nombre": "Cillian",
                    "apellido1": "Murphy ",
                    "apellido2": {},
                    "fecha_nac": "25/05/1976",
                    "edad": "47",
                    "peliculas": "Oppenheimer",
                    "oscar": "0"
                }
            ]
        },
        {
            "actor": [
                {
                    "nombre": "Penelope ",
                    "apellido1": "Cruz ",
                    "apellido2": "Sanchez ",
                    "fecha_nac": "28/04/1974",
                    "edad": "49",
                    "peliculas": "Ferrari",
                    "oscar": "1"
                },
                {
                    "nombre": "Sofia ",
                    "apellido1": "Vergara ",
                    "apellido2": "Davila",
                    "fecha_nac": "10/07/1972",
                    "edad": "51",
                    "peliculas": "Pitufos",
                    "oscar": "0"
                },
                {
                    "nombre": "Natalie ",
                    "apellido1": "Portman ",
                    "apellido2": {},
                    "fecha_nac": "9/06/1981",
                    "edad": "42",
                    "peliculas": "Thor",
                    "oscar": "1"
                },
                {
                    "nombre": "Margot",
                    "apellido1": "Robbie ",
                    "apellido2": {},
                    "fecha_nac": "2/07/1990",
                    "edad": "33",
                    "peliculas": "Barbie",
                    "oscar": "2"
                },
                {
                    "nombre": "Jennifer ",
                    "apellido1": "Aniston",
                    "apellido2": {},
                    "fecha_nac": "11/02/1969",
                    "edad": "54",
                    "peliculas": "Murder Mistery",
                    "oscar": "0"
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
