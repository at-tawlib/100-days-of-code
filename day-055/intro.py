# 29-12-22
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, world!</h1>' \
           '<p>This is a paragraph.</p>'

@app.route("/bye")
def bye():
    return "Bye!"

# adding variables
@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"

@app.route("/<name>")
def greet2(name):
    return f"Hello {name}!"

@app.route("/username/<name>/1")
def greet3(name):
    return f"Hello there {name}!"

@app.route("/pathname/<path:name>")
def greet_path(name):
    return f"Hello {name}"

# multiple variables
@app.route("/multiple/<name>/<int:number>")
def greet_multiple(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    # allow debug mode
    app.run(debug=True)