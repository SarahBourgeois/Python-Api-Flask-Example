from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.model.homeModel import HomeModel
from api.schema.homeSchema import HomeSchema

home_api = Blueprint('api', __name__)


@home_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': HomeSchema
        }
    }
})
def welcome():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    result = HomeModel()
    return HomeSchema().dump(result), 200