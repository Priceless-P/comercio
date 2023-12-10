"""Defines a User Class"""

from application import db
from datetime import datetime
from flask_login import UserMixin
from passlib.hash import sha256_crypt

class User(UserMixin, db.Model):
    """Represents a user"""
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(120), unique=False, nullable=False)
    lastname = db.Column(db.String(120), unique=False, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    authenticated = db.Column(db.Boolean, default=False)
    api_key = db.Column(db.String(120), unique=True, nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def encode_api_key(self):
        """Encodes user's api key"""
        self.api_key = sha256_crypt.hash(self.username + str(datetime.utcnow))

    def encode_password(self):
        """Encodes user's password"""
        self.password = sha256_crypt.hash(self.password)

    def __repr__(self):
        """Returns string representation of User Instance"""
        return '<User %r>' % (self.username)

    def to_json(self):
        """Returns user's details in J
        son format"""
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username': self.username,
            'email': self.email,
            'is_admin': self.is_admin,
            'api_key': self.api_key,
            'is_active': True
        }
