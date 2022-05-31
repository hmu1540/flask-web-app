# import sys
# print(sys.path)
import imp
from flask import Flask

# file: make the website folder here a python package
# whenever we import website folder, code in this file will run automatically
def create_app():
    # initialize the app
    app = Flask(__name__)
    # secure the cookies and session data related to our website, random strings, in production, dont share
    app.config['SECRET_KEY'] = 'aljsfkjdlkjflsf'
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    
    return app


