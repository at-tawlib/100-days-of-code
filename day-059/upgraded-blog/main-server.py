# 07-01-23 Blog website with Flask and Jinja
from flask import Flask, render_template
import requests

# get posts from the API
posts = requests.get("https://api.npoint.io/da865b407af4da4dba18").json()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def go_to_about():
    return render_template("about.html")

@app.route('/contact')
def go_to_contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)