from models.Interests import InterestsModel

from flask import request
from flask_restful import Resource

from config import db

class InterestList(Resource):
    def get(self):
        interests = [interest.to_dict() for interest in InterestsModel.query.all()]
        return interests, 200
    