from models.Cities import CityModel

from flask import request
from flask_restful import Resource
from config import db 

class CityList(Resource):
    def get(self):
        cities = [city.to_dict() for city in CityModel.query.all()]
        return cities, 200