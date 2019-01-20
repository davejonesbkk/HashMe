from flask import Flask 

app = Flask(__name__, instance_relative_config=True)
print(app)

from app.models import db

from app.models import MyDB

from app import views

app.config.from_object('config')

