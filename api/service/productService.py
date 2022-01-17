
   
from unicodedata import name
from api.schema.productSchema import Product
from flask import make_response
import json

# Add product 
def add_product_service(product_data):
    try:
        name = product_data['name']
        productToAdd = Product(name=name)
        productToAdd.save()
        return make_response({'message' : 'succesfully inserted'}, 201)   
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  


# Get product By ID
def get_productbyid_service(product_id):
    products = []
    try:
        product_data = Product.objects[:1](id=product_id)
        for product in product_data:
            product_data = {}
            product_data['_id'] = str(product.id)
            product_data['title'] = product.title
            product_data['description'] = product.description
            product_data['image'] = product.image
            product_data['category'] = product.category
            product_data['price'] = json.dumps(product.price)
            product_data['quantity'] = product.quantity
            products.append(product_data)

        return {"product": products}
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  