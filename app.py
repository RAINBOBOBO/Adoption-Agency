"""Flask app for adopt app."""

from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

DEFAULT_IMAGE_URL = 'https://cdn.dribbble.com/users/2095589/screenshots/4166422/user_1.png'

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:qwerty@localhost/adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route("/")
def root():
    """ Renders the html for listing the pets """
    pets = Pet.query.all()
    return render_template("list-pets.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def show_add_form():
    """ Shows a form for adding a pet to the list of pets.
        Handles form submission and makes changes in the db.
    """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added the {species} named {name}.")
        return redirect("/")
    else:
        return render_template("add-pets.html", form=form)

@app.route('/<pet_id>', methods=['GET', 'POST'])
def show_pet_detail(pet_id):
    """ Show details about a pet and a form for editing some details about that pet."""

    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data or DEFAULT_IMAGE_URL
        pet.notes = form.notes.data
        available = form.available.data
        if available == 'False':
            available = False
        else:
            available = True

        pet.available = available

        db.session.commit()

        flash("Details Updated!")
        return redirect("/")
    
    return render_template('pet-detail.html', pet=pet, form=form)
