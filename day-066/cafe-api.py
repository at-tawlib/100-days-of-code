import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    """class for Cafe table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        """Returns human readable format of the class"""
        return f'<Cafe {self.name}>'

    def to_dict(self):
        """
        convert object to dictionary to use by jsonify
        where the key is the name of the column and the value is the value of the column
        Return:
            dictionary of the object
        """
        # dictionary = {}
        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def get_random():
    """fetch random cafe from database => convert the data to dict => use jsonify to convert to json
    Return:
        json of object
    """
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # return jsonify(
    #     cafe={
    #         # omit the id from the response
    #         "name": random_cafe.name,
    #         "map_url": random_cafe.map_url,
    #         "img_url": random_cafe.img_url,
    #         "location": random_cafe.location,
    #
    #         # put some properties in a sub-category
    #         "amenities": {
    #             "seats": random_cafe.seats,
    #             "has_toilet": random_cafe.has_toilet,
    #             "has_wifi": random_cafe.has_wifi,
    #             "has_sockets": random_cafe.has_sockets,
    #             "can_take_calls": random_cafe.can_take_calls,
    #             "coffee_price": random_cafe.coffee_price,
    #         }
    #     }
    # )
    # convert the random_cafe to a dictionary
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def get_all():
    """returns all cafes in the database as JSON
    Return:
        JSON of all cafes
    """
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route('/search')
def get_cafe_at_location():
    """search for and returns cafes at a particular location.
    use this by typing in the url 'localhost:.../search?loc=Location'
    Return:
        json at the location or error json
    """
    location = request.args.get("loc")
    cafes_by_location = db.session.query(Cafe).filter_by(location=location).all()
    if cafes_by_location:
        return jsonify(cafe=[cafe.to_dict() for cafe in cafes_by_location])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})

@app.route('/add', methods=['POST'])
def post_new_cafe():
    """post new cafe to the api
    Return:
        json text to indicate a successful response
    """
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe."})

@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def patch_new_price(cafe_id):
    """
    searches for cafe with the id and updates its price with the new price using patch
    Args:
        cafe_id (int): id of cafe to update the price
    Return:
        json of successful update of price or error if failed to update

    """
    new_price = request.args.get('new_price')
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        # just add the code after the jsonify method. 200 = Ok
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        # 404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

@app.route('/report-closed/<int:cafe_id>', methods=["DELETE"])
def delete_cafe(cafe_id):
    """
    checks the api key if it matches the secret key (TopSecretAPIKey)  if it is valid,
    get cafe from database using the cafe_id, then delete the cafe if present in the database
    Args:
        cafe_id (int) : id of cafe
    Return:
        json of api error or json of success or json of failed
    """
    api_key = request.args.get('api_key')
    if  api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database"}), 200
        else:
            return jsonify(
                error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Not Found": "Sorry that's not allowed. Make sure you have the correct api_key."}), 404

if __name__ == '__main__':
    app.run(debug=True)