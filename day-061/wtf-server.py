# 10-01-2023 Demo for Flask, Jinja, Flask-WTF forms, Flask Bootstrap
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = "#########"

class LoginForm(FlaskForm):
    """class to create login form"""
    email = EmailField(label='Email', validators=[DataRequired(), Email(message="Enter valid email")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    """login page"""
    login_form = LoginForm()
    login_form.validate_on_submit()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template("denied.html")
    return render_template('login.html',form=login_form)

if __name__ == '__main__':
    app.run(debug=True)