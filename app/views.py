

from flask import render_template, request, redirect, url_for

from app import app 


from flask_login import login_user
from flask_login import logout_user

from flask_login import LoginManager
from flask_login import login_required 

from app.mockdbhelper import MockDBHelper as DBHelper
from pass_builder import PasswordHelper

from app.user import User 

app.secret_key = 'ZvOSAWwgSSfQ8qsCvLI8tQHIlj7Lu6E2KkVF+/okg1nQtUhYJaq+3PAT8KI1'


DB = DBHelper()
PH = PasswordHelper()

login_manager = LoginManager()

@app.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template("index.html") 


@app.route('/account')
@login_required 
def account():
	
	return render_template('account.html')



@app.route('/login', methods=['GET', 'POST'])
def login():


	email = request.form.get("email")
	password = request.form.get("password")
	stored_user = DB.get_user(email)

	if stored_user and PH.validate_password(password, stored_user['salt'],
		stored_user['hashed']):

		user = User(email)
		login_user(user, remember=True)
		return redirect(url_for('account'))
	#return home()
	return render_template('login.html')



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

@app.route("/register", methods=["GET", "POST"])
def register():
	email = request.form.get("email")
	pw1 = request.form.get("password")
	pw2 = request.form.get("password2")

	if not pw1 == pw2:
		return redirect(url_for('home'))
	if DB.get_user(email):
		return redirect(url_for('home'))
	salt = PH.get_salt()
	hashed = PH.get_hash(pw1 + salt)
	DB.add_user(email, salt, hashed)
	return redirect(url_for('home'))









