import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "fruteria": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "fruta": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "codigo": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "tipo": {
                                    "type": "string", 
                                    "minLength": 1
                                    },
                                "color": {
                                    "type": "string", 
                                    "minLength": 1
                                    },
                                "arbol": {
                                    "type": "string", 
                                    "minLength": 1
                                    },
                                "proveniencia": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "clasificacion": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "cultivo": {
                                    "type": "string",
                                    "minLength": 1
                                    }
                            },
                            "required": ["codigo", "tipo", "color", "arbol", "proveniencia", "clasificacion", "cultivo"]
                        }
                    }
                },
                "required": ["fruta"]
            }
        }
    },
    "required": ["fruteria"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "fruteria": [
        {
            "fruta": [
                {
                    "codigo": "001",
                    "tipo": "Acida",
                    "color": "Naranja",
                    "arbol": "Naranjo",
                    "proveniencia": "Asia",
                    "clasificacion": "Sapindales",
                    "cultivo": "citrico"
                },
                {
                    "codigo": "002",
                    "tipo": "Dulce",
                    "color": "Roja/Verde",
                    "arbol": "Manzano",
                    "proveniencia": "Asia",
                    "clasificacion": "Malus ",
                    "cultivo": "pomácea"
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
