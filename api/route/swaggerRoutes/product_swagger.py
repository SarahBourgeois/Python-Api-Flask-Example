from api.schema.productSchema import ProductSchema
product_tag = "Product"

get_all_products = {
        "tags": [product_tag],
        "responses": {
            "200": {
                "description": "Success!",
                "schema": ProductSchema
            }
        }
}

get_product_by_id = {
        "tags": [product_tag],
        "parameters": [
            {
                "name": "product_id",
                "in": "path",
                "required": True,
                "type": "number",
                "description": "id of the product"
            }
        ],
        "responses": {
            "200": {
                "description": "Success!",
                "schema": ProductSchema
            }
        }
}

add_new_product = { 
        "tags": [product_tag],
        "parameters": 
        [ 
            {
                "schema": ProductSchema,
                "name": "productDto",
                "in": "body",
                "required": False,
                "type": "object",
                "description": "product to add"
            },
        ],
        "responses": 
        {
        "200": {
            "description": "Product correctly add",
            "schema": ProductSchema
        }
    }
}