"""Flask app for adopt app."""

from flask import Flask, render_template, flash, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

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
  pets = Pet.query.all()
  return render_template("list-pets.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_form():

  form = AddPetForm()

  if form.validate_on_submit():
    name = form.name.data
    species = form.species.data
    photo_url = form.photo_url.data
    age = form.age.choices
    notes = form.notes.data

    flash(f"Added the {species} named {name}.")
    return redirect("/")
  else:
    return render_template("add-pets.html", form=form)