#! usr/bin/python3
"""
flask application
"""

#import flask
from flask import Flask

# make flask run file name
app =  Flask(__name__)

@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(debug=True)

# debug=True, host="0.0.0.0", port="5000"