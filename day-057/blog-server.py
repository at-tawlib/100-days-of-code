# 31-12-2022 Templating with Jinja in Flask
from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
@app.route("/")
def home():
    # passing a value to be used in HTML by Jinja
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)
@app.route('/guess/<name>')
def guess_age_gender(name):
    """Uses API to guess age and gender from the name entered"""
    agify_endpoint = f"https://api.agify.io?name={name}"
    age = requests.get(agify_endpoint).json()['age']
    gender_endpoint = f"https://api.genderize.io?name={name}"
    gender =  requests.get(gender_endpoint).json()['gender']
    return render_template("guess.html", name=name, age=age, gender=gender)
@app.route("/blog/<num>")
def get_blog(num):
    # passes this number to the blog url
    print(num)
    # create a json object with npoint and get the url to use here
    blog_url = "https://api.npoint.io/8832351a2fc9c67bd109"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", post=all_posts)

if __name__ == "__main__":
    app.run(debug=True)