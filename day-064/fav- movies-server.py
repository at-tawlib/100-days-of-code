# 15-01-2023 Favourite Movies of All time
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# For Movie API
MOVIE_DB_API_KEY = "674eaeac19631c12288566bf1a5317fd"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.app_context().push()  # to prevent app out of context error
app.config['SECRET_KEY'] = 'BA5DA2C5D699AF6D4A6D4A9D9AGA4'
Bootstrap(app)

# create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# create table
class Movie(db.Model):
    """"class to create db object and table"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'


db.create_all()


class FindMovieForm(FlaskForm):
    """form class for find movies"""
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


class RateMovieForm(FlaskForm):
    """form class for edit movie form"""
    rating = StringField(label="Your Rating Out of 10 e.g 7.5")
    review = StringField(label="Your Review")
    submit = SubmitField(label="Done")


@app.route('/')
def home():
    """index or homepage of website"""
    # get all movies and send to index page
    # all_movies = db.session.query(Movie).all()
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    """Adds a new movie to the database"""
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(url=MOVIE_DB_SEARCH_URL, params={
            'api_key': MOVIE_DB_API_KEY,
            'query': movie_title
        })
        response.raise_for_status()
        data = response.json()['results']
        return render_template('select.html', options=data)
    return render_template('add.html', form=form)

@app.route('/find')
def find_movie():
    """Find movie by id an add to database"""
    movie_api_id = request.args.get('id')
    if movie_api_id:
        # get movie by id from the api
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(url=movie_api_url, params={
            'api_key': MOVIE_DB_API_KEY,
            "language": "en-US"
        })
        data = response.json()
        # add movie to the database
        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('rate_movie', id=new_movie.id))



@app.route("/edit", methods=("POST", "GET"))
def rate_movie():
    """Update a movie"""
    rate_form = RateMovieForm()
    # get movie from id from the index page
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if rate_form.validate_on_submit():
        movie.rating = float(rate_form.rating.data)
        movie.review = rate_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=rate_form)


@app.route('/delete')
def delete_movie():
    """Delete a movie from the movies database"""
    movie_id = request.args.get('id')
    # delete movie
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/select')
def select_movie():
    movies = request.args.get('movies')
    return render_template('select.html', movies=movies)




if __name__ == "__main__":
    app.run(debug=True)
