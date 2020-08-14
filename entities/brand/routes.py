from app import db, app
from flask import jsonify, request
from entities.brand.schema import brand_schema, brands_schema
from entities.brand.model import Brand


@app.route('/brands', methods=['POST'])
def getBrands():
    brands = Brand.query.all()
    return brands_schema.jsonify(brands)


@app.route('/brand', methods=['POST'])
def getBrand():
    id = request.json['id']
    brand = Brand.query.get(id)
    return brand_schema.jsonify(brand)


@app.route('/addBrand', methods=['POST'])
def addBrand():
    name = request.json['name']
    country = request.json['country']

    new_brand = Brand(name, country)

    db.session.add(new_brand)
    db.session.commit()

    return brand_schema.jsonify(new_brand)


@app.route('/updateBrand', methods=['POST'])
def updateBrand():
    id = request.json['id']
    name = request.json['name']
    country = request.json['country']

    brand = db.session.query(Brand).filter(Brand.id == id).one()
    brand.name = name
    brand.country = country
    db.session.commit()

    return brand_schema.jsonify(brand)

@app.route('/deleteBrand', methods=['POST'])
def deleteBrand():
    id = request.json['id']
    db.session.query(Brand).filter(Brand.id == id).delete()
    db.session.commit()

    current_brands = Brand.query.all()
    return brands_schema.jsonify(current_brands)
