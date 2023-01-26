# 25-02-2023 Authentication with flask
from flask import Flask, render_template, request, url_for, redirect, send_from_directory, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.app_context().push()  # to prevent app out of context error
app.config['SECRET_KEY'] = "jajg54gakjfgf95j4f*4jz9jf965"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# configure LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """load user by returning the user id
    Return:
        user id (int)
    """
    return User.query.get(int(user_id))


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    """Create users to add to table"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    name = db.Column(db.String(1000))


# below line only required once to create the database
db.create_all()


@app.route('/')
def home():
    """renders the index page"""
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["POST", "GET"])
def register():
    """renders register.html"""
    if request.method == "POST":
        # check if email already exists in the database
        if User.query.filter_by(email=request.form.get('email')).first():
            # flash user already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        # Use hashing and salting to generate a salted Hashed password
        hash_and_salted_password = generate_password_hash(
            password=request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            password=hash_and_salted_password,
            name=request.form.get('name'),
        )
        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database
        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # find user email entered from the db
        user = User.query.filter_by(email=email).first()

        # if email does not exist
        if not user:
            flash("That email does not exist, please try again")
            return redirect(url_for('login'))
        elif not check_password_hash(pwhash=user.password, password=password):
            # if password does not match with the one in the db
            flash("Password incorrect, please try again.")
            return redirect(url_for('login'))
        else:
            # email exists and password is correct
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html", loggen_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    """open file if authentication is correct"""
    return send_from_directory(directory='static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
