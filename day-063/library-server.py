# 14-01-2023 Build SQLITE Database into Flask website
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
# Create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collections.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create Table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

@app.route('/')
def home():
    # read all records
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        # create record and add to database
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        # Update Record
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))

    # read record by id
    book_id = request.args.get('id')
    selected_book = Book.query.get(book_id)
    return render_template('edit.html', book=selected_book)

@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    # Delete record by ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)