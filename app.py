from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<H1>This is Adam's world</H1>"

