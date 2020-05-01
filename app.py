from flask import Flask
from flask import render_template
from flask import jsonify
app = Flask(__name__)

from random import randint

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random/<size>')
def random(size):
    randList = []
    for x in range(0, int(size)):
        randList.append(randint(0,20))
    return jsonify(randList)

@app.route('/gravity/<distance>')
def gravity(distance):
    return  jsonify(1 * 10 * 10 / float(distance)**2)
