from models.Country import CountryModel
from config import db 
from flask import request
from flask_restful import Resource

class CountriesList(Resource):
    def get(self):
        countries = [country.to_dict() for country in CountryModel.query.all()]
        return countries, 200
    
    def post(self):
        json = request.get_json()
        try:
            new_country = CountryModel(
                country_name = json.get("countryName"),
                country_img = json.get("countryImg"),
                country_intro = json.get("countryIntro")
            )
            db.session.add(new_country)
            db.session.commit()
            return {"message": "New Country added"}, 201
        except ValueError as e:
            return {"error": [str(e)]}, 400

        
        