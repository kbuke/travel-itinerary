from models.Site import SitesModel
from config import db
from flask import request
from flask_restful import Resource

class SitesList(Resource):
    def get(self):
        sites = [site.to_dict() for site in SitesModel.query.all()]
        return sites, 201
    
    def post(self):
        json = request.get_json()

        try:
            new_site = SitesModel(
                site_name = json.get("siteName"),
                site_img = json.get("siteImg"),
                address_line_1 = json.get("address1"),
                address_line_2 = json.get("address2"),
                address_line_3 = json.get("address3"),
                post_code = json.get("postCode"),
                country_id = json.get("countryId"),
                city_id = json.get("cityId")
            )
            db.session.add(new_site)
            db.session.commit()
            return {"message": "New site created"}, 201
        except ValueError as e:
            return {"error": [str(e)]}, 400

class Sites(Resource):
    def delete(self, id):
        site = SitesModel.query.filter(SitesModel.id == id).first()
        if site:
            db.session.delete(site)
            db.session.commit()
            return {"message": f"Site {id} deleted"}, 200
        else:
            return {"error": f"Site {id} not found"}, 404