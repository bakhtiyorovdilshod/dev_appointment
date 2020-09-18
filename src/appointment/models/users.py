from . import db



class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String())
    phone_number = db.Column(db.String())


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String())
    age = db.Column(db.Integer())
    phone_number = db.Column(db.String())
    contact = db.Column(db.Integer(), db.ForeignKey('contacts.id'))
