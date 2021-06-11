from flask import Flask
from diary.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app) # flask-login adds the current_user variable to your templates:
login.login_view = 'login' # when access a login_required view without being logged in, redirect to login view => url_for('login')


# urls, models 호출
from diary import urls, models