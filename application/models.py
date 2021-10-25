from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class Customer(db.Model):
    __tablename__ = "Customer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_time = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(16), nullable=True)
    c_time = db.Column(db.DateTime, nullable=True)
    skey = db.Column(db.String(6), nullable=True)

    def change_status(self, status):
        self.status = status

    def get_id(self):
        return self.id

    def __repr__(self):
        return "<Customer {}}>".format(self.id)


class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, unique=False)
    created_on = db.Column(db.DateTime, nullable=True, unique=False)
    last_login = db.Column(db.DateTime, nullable=True, unique=False)

    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.id)