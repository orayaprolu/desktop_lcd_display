from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is my Flask app running on my local network!'

@app.route("/<name>")
def hello2(name):
    return f"Hello, {escape(name)}!"
