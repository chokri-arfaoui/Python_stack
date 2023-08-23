from flask import Flask

app = Flask(__name__)

app.secret_key = "belt_demo"
DATABASE = "registration_db"