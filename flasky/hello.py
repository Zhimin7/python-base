from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/user/<name>/')
def user(name):
    return render_template('user.html', name=name)


@app.route('/'):
def index():
	return '<h1>Hello world</h1>'

