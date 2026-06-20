# this code is from shubham's git
# flask app
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    return none
if none:
    go


@app.route('/health')
def health():
    return 'Server is up and running'
