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