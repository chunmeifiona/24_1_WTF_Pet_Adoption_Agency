"""Pet Adoption Agency application"""
from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm,EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'It is secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

DEFAULT_PHOTO_URL = "https://images.unsplash.com/photo-1563460716037-460a3ad24ba9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fHBldHN8ZW58MHx8MHx8&auto=format&fit=crop&w=400&q=60"

@app.route('/')
def show_home_page():
    """Show home page Listing Pets"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Create a form for adding pets"""
    form= AddPetForm()
    if form.validate_on_submit():
        # raise
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data if form.photo_url.data else DEFAULT_PHOTO_URL
        age = form.age.data
        notes = form.notes.data
        pet=Pet(name=name, species=species,photo_url=photo_url,age=age,notes=notes)

        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Display/Edit Form"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url=form.photo_url.data
        pet.notes=form.notes.data
        pet.available=form.available.data

        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_pet.html", form=form, pet=pet)

