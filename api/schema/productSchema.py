from marshmallow.fields import Nested, Str, Number
from flask_marshmallow import Schema
from marshmallow.fields import Str

class ProductSchema(Schema):
    class Product:
        # Fields to expose
        fields = ["index", "name", "price", "category"]

    index = Number()
    name = Str()
    price = Number()
    category = Str()
