from models.Site import SitesModel
from config import db
from flask import request
from flask_restful import Resource

class SitesList(Resource):
    def get(self):
        sites = [site.to_dict() for site in SitesModel.query.all()]
        return sites, 201