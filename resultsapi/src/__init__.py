from flask import Flask
from models import db
from config import DATABASE_CONNECTION_URI

def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # adding context to future calls made with this app (line 11) flask.current_app=the application handling the current request
    flask_app.app_context().push() # since Flask can have multiple apps we have to specify which app we are using with SQLAlchemy, hence we push the context with our newly created app. 
    db.init_app(flask_app) # linking db to flask app
    db.drop_all() # deleting all databases so we start with an empty database
    db.create_all() # creating table(s) in database, using models.py
    return flask_app