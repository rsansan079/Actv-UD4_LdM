import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "biblioteca": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "libro": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "cod_libro": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "titulo": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "editorial": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "edicion": {
                                    "type": "string",
                                    "minLength": 1
                                    },
                                "ISBN": {
                                    "type": "string", 
                                    "minLength": 1
                                    },
                                "num_pg": {
                                    "type": "string", 
                                    "minLength": 1
                                    },
                                "autor": {
                                    "type": "string", 
                                    "minLength": 1
                                    }
                            },
                            "required": ["cod_libro", "titulo", "editorial", "edicion", "ISBN", "num_pg", "autor"]
                        }
                    }
                },
                "required": ["libro"]
            }
        }
    },
    "required": ["biblioteca"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "biblioteca": [
        {
            "libro": [
                {
                    "cod_libro": "22622",
                    "titulo": "100 años de Soledad",
                    "editorial": "Sudamericana",
                    "edicion": "ilustrada",
                    "ISBN": "978-84-9759-220-8",
                    "num_pg": "496",
                    "autor": "Gabriel Garcia"
                },
                {
                    "cod_libro": "33643",
                    "titulo": "Poesías Completas",
                    "editorial": "Debolsillo",
                    "edicion": "ilustrada",
                    "ISBN": "9788467021509",
                    "num_pg": "346",
                    "autor": "Antonio Machado"
                },
                {
                    "cod_libro": "54732",
                    "titulo": "Fuenteovejuna",
                    "editorial": "Verbum",
                    "edicion": "ilustrada",
                    "ISBN": "9788467528572",
                    "num_pg": "508",
                    "autor": "Lope de Vega"
                },
                {
                    "cod_libro": "12543",
                    "titulo": "La Casa de los Espíritus",
                    "editorial": "Agapea",
                    "edicion": "ilustrada",
                    "ISBN": "9788483462034",
                    "num_pg": "358",
                    "autor": "Lope de Vega"
                },
                {
                    "cod_libro": "99678",
                    "titulo": "El Buscón",
                    "editorial": "Octaedro",
                    "edicion": "ilustrada",
                    "ISBN": "9788466792479",
                    "num_pg": "523",
                    "autor": "Quevedo"
                }
            ]
        },
        {
            "libro": [
                {
                    "cod_libro": "93469",
                    "titulo": "Don Quijote de la Mancha",
                    "editorial": "Urbano Manini",
                    "edicion": "ilustrada",
                    "ISBN": "9788493806125",
                    "num_pg": "789",
                    "autor": "Cervantes"
                },
                {
                    "cod_libro": "20638",
                    "titulo": "Hamlet",
                    "editorial": "Espasa",
                    "edicion": "ilustrada",
                    "ISBN": "9788467033380",
                    "num_pg": "326",
                    "autor": "Shakespeare"
                },
                {
                    "cod_libro": "43334",
                    "titulo": "Las Almas Muertas",
                    "editorial": "ALIANZA",
                    "edicion": "ilustrada",
                    "ISBN": "9788420653419",
                    "num_pg": "456",
                    "autor": "Nikolai Gogol"
                },
                {
                    "cod_libro": "72101",
                    "titulo": "5 Horas con Mario",
                    "editorial": "Destino",
                    "edicion": "ilustrada",
                    "ISBN": "9788423342402",
                    "num_pg": "332",
                    "autor": "Miguel Delibes"
                },
                {
                    "cod_libro": "93993",
                    "titulo": "Tan Poca Vida",
                    "editorial": "ALIANZA",
                    "edicion": "ilustrada",
                    "ISBN": "9788423366402",
                    "num_pg": "221",
                    "autor": "Hanya Yanagihara"
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