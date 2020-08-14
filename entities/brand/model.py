from app import db

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    country = db.Column(db.String(100))

    def __init__(self, name, country):
        self.name = name
        self.country = country