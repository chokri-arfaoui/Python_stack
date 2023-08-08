from flask_app import DB
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create(cls, data):
        query="""
            INSERT INTO dojos (name) VALUES (%(name)s)
            """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        result = connectToMySQL(DB).query_db(query)
        print(result)
        all_dojos = []
        for row in result:
            all_dojos.append(cls(row))
        print(all_dojos)
        return all_dojos
    
    @classmethod
    def dojo_with_its_ninjas_by_id(cls, data):
        query = """
                SELECT * FROM dojos
                LEFT JOIN ninjas ON dojo_id = dojos.id
                WHERE dojos.id = %(id)s
                """
        result = connectToMySQL(DB).query_db(query, data)
        dojo = cls(result[0])
        for row in result:
            ninjas = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'dojo_id': row['dojo_id'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninjas))
        return dojo

