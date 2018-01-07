

from flask import render_template, request 

from app import app 

from flask.ext.login import login_user

from mockdbhelper import MockDBHelper as DBHelper
from user import User 



login_manager = LoginManager()

@app.route('/')
def hello_world():
    
    return render_template("index.html") 


login_manager.init_app(app)


@login_manager.user_loader 
def load_user(user_id):
	return User.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():

	form = LoginForm()
	if form.validate_on_submit():
		login_user(user)

		flask.flash('Logged in')

		next = flask.request.args.get('next')

		if not is_safe_url(next):
			return flask.abort(400)

		return flask.redirect(next or flask.url_for('index'))
	return flask.render_template('login.html', form=form)


