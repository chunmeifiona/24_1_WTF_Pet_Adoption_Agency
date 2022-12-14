"""Models for Pet Adoption Agency"""
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def connect_db(app):
    """
    Connect this database to provided Flask app.
    You should call this in your Flask app.
    """
    db.app=app
    db.init_app(app)

class Pet(db.Model):
    """Adoptable pet."""
    __tablename__='pets'
    def __repr__(self):
        p=self
        return f"<Pet {p.id} {p.name} {p.photo_url} {p.age} {p.available}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.Text, nullable=False)
    species=db.Column(db.Text, nullable=False)
    photo_url=db.Column(db.Text)
    age=db.Column(db.Integer)
    notes=db.Column(db.Text)
    available=db.Column(db.Boolean,nullable=False, default=True)