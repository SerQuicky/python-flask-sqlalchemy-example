
from app import app, db
from flask import jsonify, request
from entities.vehicle.schema import vehicle_schema, vehicles_schema
from entities.vehicle.model import Vehicle


@app.route('/vehicles', methods=['GET'])
def getVehicles():
    vehicles = Vehicle.query.all()
    return vehicles_schema.jsonify(vehicles)


@app.route('/vehicle', methods=['POST'])
def getVehicle():
    id = request.json['id']
    vehicle = Vehicle.query.get(id)
    return vehicle_schema.jsonify(vehicle)


@app.route('/vehiclesByBrand', methods=['POST'])
def getVehiclesByBrand():
    brandId = request.json['brandId']
    vehicles = db.session.query(Vehicle).filter(Vehicle.brandId == brandId).all()
    return vehicles_schema.jsonify(vehicles)


@app.route('/addVehicle', methods=['POST'])
def addVehicle():
    name = request.json['name']
    model = request.json['model']
    manufactureYear = request.json['manufactureYear']
    brandId = request.json['brandId']

    new_vehicle = Vehicle(name, model, manufactureYear, brandId)

    db.session.add(new_vehicle)
    db.session.commit()

    return vehicle_schema.jsonify(new_vehicle)


@app.route('/updateVehicle', methods=['POST'])
def updateVehicle():
    id = request.json['id']
    name = request.json['name']
    model = request.json['model']
    manufactureYear = request.json['manufactureYear']
    brandId = request.json['brandId']

    vehicle = db.session.query(Vehicle).filter(Vehicle.id == id).one()
    vehicle.name = name
    vehicle.model = model
    vehicle.manufactureYear = manufactureYear
    vehicle.brandId = brandId

    db.session.commit()

    return vehicle_schema.jsonify(vehicle)


@app.route('/deleteVehicle', methods=['POST'])
def deleteVehicle():
    id = request.json['id']
    db.session.query(Vehicle).filter(Vehicle.id == id).delete()
    db.session.commit()

    current_vehicles = Vehicle.query.all()
    return vehicles_schema.jsonify(current_vehicles)
