from app import app, views
from flask_sqlalchemy import SQLAlchemy 


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #needs to be false to avoid warnings
db = SQLAlchemy(app)

class MyDB(db.Model):
	email = db.Column(db.String(100), primary_key=True, unique=True)
	password  = db.Column(db.String(100))

	#def __init__(self, email, password):
		#self.email = email 

	def __repr__(self):
		return '<MyDB %r>' % self.email 

		



