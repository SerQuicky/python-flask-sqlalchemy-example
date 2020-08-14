from app import ma

class BrandSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'country')

brand_schema = BrandSchema()
brands_schema = BrandSchema(many=True)