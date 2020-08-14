from app import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    model = db.Column(db.String(100), unique=True)
    manufactureYear = db.Column(db.Integer)
    brandId = db.Column(db.Integer, db.ForeignKey('brand.id'))

    def __init__(self, name, model, manufactureYear, brandId):
        self.name = name
        self.model = model
        self.manufactureYear = manufactureYear
        self.brandId = brandId