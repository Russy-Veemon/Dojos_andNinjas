from flask_app.config.MySQLConnection import connectToMySQL


class Ninja:
    def __init__(self, data:dict):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results:list[dict] = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninja_objects:list[Ninja] = []
        for ninja in results:
            ninja_objects.append(cls(ninja))

        return ninja_objects
    
    @classmethod
    def insert_ninja(cls, data:dict):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def show_one(cls, data:dict):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data:dict):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, created_at=NOW(), updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def delete_ninja(cls, data:dict):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)
