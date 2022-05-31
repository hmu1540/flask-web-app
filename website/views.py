# file: all the views or URL end point for the functioning frontend aspect of our website
#  

from flask import Blueprint

views = Blueprint('views', __name__)  #?????

@views.route('/')
def home():
    return "<h1>Test</h1>"
# now go regiter it in __init__.py