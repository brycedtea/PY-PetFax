
#this is a test

from flask import ( Blueprint, render_template ) 

bp = Blueprint('about', __name__, url_prefix="/about")

@bp.route('/about')
def new(): 
    return render_template('about/about.html')