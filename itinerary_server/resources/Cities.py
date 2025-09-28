from models.Cities import CityModel

from flask import request
from flask_restful import Resource
from config import db 

class CityList(Resource):
    def get(self):
        cities = [city.to_dict() for city in CityModel.query.all()]
        return cities, 200
    
    def post(self):
        json = request.get_json()

        try:
            new_city = CityModel(
                city_name = json.get("cityName"),
                city_img = json.get("cityImg"),
                city_intro = json.get("cityIntro"),
                population = json.get("population"),
                country_id = json.get("countryId")
            )
            db.session.add(new_city)
            db.session.commit()
            return{"message": "New city created"}, 201
        except ValueError as e:
            return{"error": [str(e)]}, 401

class City(Resource):
    def delete(self, id):
        city = CityModel.query.filter(CityModel.id==id).first()
        if city:
            db.session.delete(city)
            db.session.commit()
            return {"message": f"City {id} deleted"}, 200
        else:
            return {"error": f"City {id} not found"}, 404