import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
# SQLALCHEMY_DATABASE_URI = 'your psycopg2 URI connection'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask_mvc'
# SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/flask_mvc'
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False