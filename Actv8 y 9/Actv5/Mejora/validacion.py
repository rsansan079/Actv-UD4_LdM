import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "libros": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "libro": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "ISBN": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "Titulo": {
                                    "type": "string", 
                                    "minLength": 1
                                    },
                                "Autor": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "Editorial": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "Observaciones": {
                                    "type": "string"
                                    },
                                "Precio": {
                                    "type": "string",
                                    "minLength": 1
                                    }
                            },
                            "required": ["ISBN", "Titulo", "Autor", "Editorial", "Precio"]
                        }
                    }
                },
                "required": ["libro"]
            }
        }
    },
    "required": ["libros"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "libros": [
        {
            "libro": [
                {
                    "ISBN": "978-3-16-148410-0",
                    "Titulo": "El Señor de los Anillos",
                    "Autor": "J.R.R. Tolkien",
                    "Editorial": "Minotauro",
                    "Observaciones": "Edición especial con ilustraciones.",
                    "Precio": "25.99"
                },
                {
                    "ISBN": "978-0-385-00855-2",
                    "Titulo": "Cien Años de Soledad",
                    "Autor": "Gabriel García Márquez",
                    "Editorial": "Critica",
                    "Precio": "19.95"
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