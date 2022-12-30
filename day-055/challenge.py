# 30-12-22 Write a decorator for html tags
from flask import Flask

app = Flask(__name__)

# Decorators to add a tag around text on web page
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route('/')
def hello_world():
    # Rendering HTML elements
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \

@app.route('/bye')
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)