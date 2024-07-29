from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['RESULT_FOLDER'] = 'result/'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///surveryDB.db'
# app.config['SECRET_KEY'] = 'This is a secret'

# db = SQLAlchemy(app)
# app.app_context().push()

from application import routes