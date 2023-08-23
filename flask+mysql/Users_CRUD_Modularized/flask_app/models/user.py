from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']


    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    

    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM users WHERE id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data_dict):
        query = """SELECT * FROM users WHERE email=%(email)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        if result :
            return cls(result[0])
        return False
    @classmethod
    def update(cls,data_dict):
        query= """UPDATE users
                SET 
                first_name= %(first_name)s, last_name= %(last_name)s,
                email= %(email)s
                WHERE id= %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def delete(cls,data_dict):
        query= """DELETE FROM users WHERE id= %(id)s; """
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['first_name'])<2:
            is_valid =False
            flash("First Name not valid", "first_name")
        if len(data_dict['last_name'])<2:
            is_valid =False
            flash("Last name not valid", "last_name")
        if not EMAIL_REGEX.match(data_dict['email']): 
            is_valid = False
            flash("Email not valid", "email")
        # if data_dict email exist in the the database 
        elif User.get_by_email({'email': data_dict['email']}):
            is_valid = False
            flash("email already taken ","email")
        
        return is_valid
    

    

    
