

from flask import render_template, request, redirect, url_for

from app import app 


from flask.ext.login import login_user
from flask.ext.login import logout_user

from flask.ext.login import LoginManager
from flask.ext.login import login_required 

from app.mockdbhelper import MockDBHelper as DBHelper
from app.user import User 

app.secret_key = 'ZvOSAWwgSSfQ8qsCvLI8tQHIlj7Lu6E2KkVF+/okg1nQtUhYJaq+3PAT8KI1'


DB = DBHelper()

login_manager = LoginManager()

@app.route('/')
def home():
    
    return render_template("index.html") 


@app.route('/account')
@login_required 
def account():
	return "Logged in"



@app.route('/login', methods=['GET', 'POST'])
def login():

	error = None

	try:


		email = request.form.get("email")
		password = request.form.get("password")
		user_password = DB.get_user(email)

		if user_password and user_password == password:
			user = User(email)
			login_user(user)
			return redirect(url_for('account'))
		else:
			error = 'Invalid login credentials. Please try again'

		return render_template("login.html")

	except Exception as e:

		return render_template('login.html', error = error)

#Required after app object has been created otherwise will get user_loader error 
login_manager.init_app(app)

@login_manager.user_loader 
def load_user(user_id):
	user_password = DB.get_user(user_id)
	if user_password:
		return User(user_id)

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for("home"))







