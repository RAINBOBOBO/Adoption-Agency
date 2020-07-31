"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://cdn.dribbble.com/users/2095589/screenshots/4166422/user_1.png'


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    species = db.Column(db.String(30), nullable=False)
    photo_url = db.Column(db.String(250), nullable=False, default=DEFAULT_IMAGE_URL)
    age = db.Column(db.String(30), nullable=False) #make a dropdown for this one
    notes = db.Column(db.String(300), nullable=False, default='')
    available = db.Column(db.Boolean(), nullable=False, default=True)

    def __repr__(self):
        """Show info about the pet."""

        p = self
        return f"<Per {p.name} {p.species} {p.photo_url} {p.age} {p.notes} {p.available}>"