import os

basedir = os.path.abspath(os.path.dirname(__file__)) # diary abspath

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'sqlite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(basedir, 'static/images')