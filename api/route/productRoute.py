from flask import Blueprint
from flasgger import swag_from
from api.route.swaggerRoutes.product import *


from api.model.productModel import ProductModel
from api.schema.productSchema import ProductSchema

product_api = Blueprint('api/product/', __name__)

@product_api.route('getAll')
@swag_from(productSwagger["get_all_products"])
def welcome():
    result = ProductModel()
    return ProductSchema().dump(result), 200

