from flask import Flask, render_template, request, session, redirect
from flask.helpers import url_for
from flask.signals import request_finished
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route("/", methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        if request.method == 'POST':
            username = (request.form['username'])
            return render_template('index.html', data=username)
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        try:
            data = User.query.filter_by(username=username, pasword=password).first()
            if data is not None:
                session['logged_in'] = True
                return redirect(url_for('index'))
            else:
                return 'Dont Login'
        except:
            return 'Dont Login'
        
        
        