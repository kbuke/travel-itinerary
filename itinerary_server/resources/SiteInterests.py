from models.SiteInterests import SiteInterestsModel

from flask import request 
from flask_restful import Resource

from config import db

class SiteInterestsList(Resource):
    def get(self):
        site_interests = [site_interest.to_dict() for site_interest in SiteInterestsModel.query.all()]
        return site_interests, 201