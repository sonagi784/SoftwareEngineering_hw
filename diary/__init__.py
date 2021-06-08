from flask import Flask, render_template, flash, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from diary.models import User, LoginForm
from diary.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/login', methods=['GET', 'POST'])
def login(): 
    loginform = LoginForm()
    if loginform.validate_on_submit() == True:
        flash('Login requested for user {}, remember_me={}'.format(loginform.username.data, loginform.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=loginform)