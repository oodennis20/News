from flask import render_template
from app import app

#our views
@app.route('/')
def index():
    '''
    Root function returning home page with data
    '''
    return render_template('index.html')
