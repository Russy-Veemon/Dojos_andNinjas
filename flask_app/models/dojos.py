from flask_app.config.MySQLConnection import connectToMySQL
from flask_app.models import ninjas


class Dojo:
    def __init__(self, data:dict):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_dojos_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db( query , data )
        dojo = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninjas.Ninja( ninja_data ) )
        return dojo
#make sure to call in HTML {%for ninja in dojo.ninjas%}
#set variable dojo = to Dojo.function(data)

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results:list[dict] = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojo_objects:list[Dojo] = []
        for dojo in results:
            dojo_objects.append(cls(dojo))

        return dojo_objects
    
    @classmethod
    def insert_dojo(cls, data:dict):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def show_one(cls, data:dict):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return cls(result[0])

