from flask import Flask
from flask import render_template
app = Flask(__name__)

from random import randint

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random')
def calculate():
    return str(randint(0,20))
