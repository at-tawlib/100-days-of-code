# 31-12-2022 Templating with Jinja in Flask
from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # passing a value to be used in HTML by Jinja
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)