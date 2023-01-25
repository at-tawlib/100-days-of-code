# 25-02-2023 Authentication with flask
from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)

app.app_context().push()  # to prevent app out of context error
app.config['SECRET-KEY'] = "jajg54gakjfgf95j4f*4jz9jf965"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    """Create users to add to table"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# below line only required once to create the database
db.create_all()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=["POST", "GET"])
def register():
    """renders register.html"""
    if request.method == "POST":
        new_user = User(
            email=request.form.get('email'),
            password=request.form.get('password'),
            name=request.form.get('name')
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("secrets"))
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/secrets')
def secrets():
    return render_template("secrets.html")

@app.route('/logout')
def logout():
    return render_template("logout.html")

@app.route('/download')
def download():
    """open file if authentication is correct"""
    return send_from_directory(directory='static', path="files/cheat_sheet.pdf")

if __name__ == "__main__":
    app.run(debug=True)