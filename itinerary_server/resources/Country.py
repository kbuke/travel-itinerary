from models.Country import CountryModel
from config import db 
from flask import request
from flask_restful import Resource

class CountriesList(Resource):
    def get(self):
        countries = [country.to_dict() for country in CountryModel.query.all()]
        return countries, 201