# import sys
# print(sys.path)
import os
import imp
from flask import Flask

# file: make the website folder here a python package
# whenever we import website folder, code in this file will run automatically
def create_app():
    # initialize the app
    app = Flask(__name__, instance_relative_config=True)
    # secure the cookies and session data related to our website, random strings, in production, dont share
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'website.sqlite')
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .import db
    db.init_app(app)
    
    return app


