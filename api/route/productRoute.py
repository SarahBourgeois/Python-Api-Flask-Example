from flask import Blueprint, jsonify, request
from flasgger import swag_from
from api.route.swaggerRoutes.product_swagger import *
from api.service.productService import add_product_service

from api.model.productModel import Product
from api.schema.productSchema import ProductSchema

product_api = Blueprint('api/v1/product/', __name__)

# Get all products 
@product_api.route('getAll')
@swag_from(get_all_products)
def welcome():
    result = Product()
    return ProductSchema().dump(result), 200

# Get product by ID
@product_api.route('<product_id>', methods = ['GET'])
@swag_from(get_product_by_id)
def getProductById(product_id):
    return jsonify({'username': product_id})

# Add product
@product_api.route('add', methods = ['POST'])
@swag_from(add_new_product)
def addProduct():
    data = request.get_json()
    return add_product_service(data)
