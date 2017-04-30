from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Test user'} # Remove this.
    template = render_template("index.html", user=user)
    return template
