from app import ma

class VehicleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'model', 'manufactureYear', 'brandId')

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)
