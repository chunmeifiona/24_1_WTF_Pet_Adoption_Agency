"""Pet Adoption Agency application"""
from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'It is secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """Show home page"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form= AddPetForm()
    if form.validate_on_submit():
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)

# @app.route("/<int: pet_id>", methods=["GET","POST"])
# def edit_pet(pet_id):
#     pet=Pet.query.get_or_404(pet_id)
#     form=Pet(obj=pet)

#     if form.validate_on_submit():
#         pet.photo_url=form.photo_url.data
#         pet.notes=form.notes.data
#         pet.available=form.available.data

#         db.session.commit()
#         return redirect("/")
#     else:
#         return render_template("edit_pet.html",form=form)

