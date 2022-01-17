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
    result = HomeModel()
    return HomeSchema().dump(result), 200