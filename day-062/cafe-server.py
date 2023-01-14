# 13-01-2023 Coffee & Wifi website
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = "#########"

class CafeForm(FlaskForm):
    """Class to create form fields for add.html"""
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = URLField(label='Cafe Location On Google Maps(URL)', validators=[DataRequired()])
    open = StringField(label='Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField(label='Closing Time e.g. 8PM', validators=[DataRequired()])
    coffee_ranking = SelectField(label="Coffee Rating", choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕','☕☕☕☕☕'], validators=[DataRequired()])
    wifi_strength = SelectField(label="Wifi Strength Rating", choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], validators=[DataRequired()])
    power = SelectField(label="Power Socket Availability", choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField(label='Submit')


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=('POST', 'GET'))
def add_cafe():
    """open form in add.html to add new café to the list of cafés"""
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        with open('cafe-data.csv', mode='a') as csv_file:
            csv_file.write(f"\n{cafe_form.cafe.data},"
                           f"{cafe_form.location.data},"
                           f"{cafe_form.open.data},"
                           f"{cafe_form.close.data},"
                           f"{cafe_form.coffee_ranking.data},"
                           f"{cafe_form.wifi_strength.data},"
                           f"{cafe_form.power.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=cafe_form)

@app.route('/cafes')
def cafes():
    """Shows list of cafés in a table"""
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == "__main__":
    app.run(debug=True)