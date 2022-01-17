from flask import Flask
from flasgger import Swagger
from api.route.homeRoute import home_api
from api.route.productRoute import  product_api

def create_app():
    app = Flask(__name__)


    app.config['SWAGGER'] = {
        'title': 'Python API with flask',
        'version' : '1.0.0' ,
    }
    swagger = Swagger(app)

    app.register_blueprint(home_api, url_prefix='/api')
    app.register_blueprint(product_api, url_prefix='/api/v1/product/')
    
    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
