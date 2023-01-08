# 07-01-23 Blog website with Flask and Jinja
from flask import Flask, render_template, request
import requests
import smtplib

# get posts from the API
posts = requests.get("https://api.npoint.io/da865b407af4da4dba18").json()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def go_to_about():
    return render_template("about.html")
@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/contact', methods=["POST", "GET"])
def go_to_contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login("$$$$$$", "##33###")
        connection.sendmail("##$##$##", "$$$$$$44", email_message)

if __name__ == "__main__":
    app.run(debug=True)