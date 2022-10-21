"""Flask app for adopt app."""

from flask import Flask, render_template, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/")
def show_base():
    """Show base page"""
    pets = Pet.query.all()
    return render_template("pets.html", pets = pets )

@app.get("/add")
def show_add_form():
    """Show pet add page"""
    form = AddPetForm()
    return render_template("form.html", form=form)

@app.post("/add")
def validate_form_input():
    """Validate new pet information"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(
            name=name, species=species, photo_url=photo_url,age=age,notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("form.html",form=form)

@app.get("/<int:pet_id_number>")
def show_pet_details(pet_id_number):
    """Display information about pet"""
    pet = Pet.query.get(pet_id_number)
    form = AddPetForm()

    form.photo_url.data = pet.photo_url
    form.notes.data = pet.notes
    form.available.data = pet.available

    return render_template("pet_detail.html",pet=pet, form=form)

