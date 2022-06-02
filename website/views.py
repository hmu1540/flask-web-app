# file: all the views or URL end point for the functioning frontend aspect of our website
#  

from flask import Blueprint
from flask.templating import render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')
# now go regiter it in __init__.py