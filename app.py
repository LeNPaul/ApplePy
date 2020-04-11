from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    value = 100 * 1234
    return render_template('index.html', name=value)
