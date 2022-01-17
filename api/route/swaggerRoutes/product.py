from api.schema.productSchema import ProductSchema


productSwagger = {
    "get_all_products": {
        "tags": ["Product"],
        "responses": {
            "200": {
                "description": "Success!",
                "schema": ProductSchema
            }
        }
    }
}