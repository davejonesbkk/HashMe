from app import app, views
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy(app)

class MyDB(db.model):
	email = db.Column(db.String(100), primary_key=True, unique=True)
	password  = db.Column(db.String(100))

	def __init__(self, email, password):
		self.email = email 



