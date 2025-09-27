from models.Interests import InterestsModel

from flask import request
from flask_restful import Resource

from config import db

class InterestList(Resource):
    def get(self):
        interests = [interest.to_dict() for interest in InterestsModel.query.all()]
        return interests, 200
    
    def post(self):
        json = request.get_json()

        try:
            new_interest = InterestsModel(
                interest = json.get("interest"),
                interest_img = json.get("interestImg")
            )
            db.session.add(new_interest)
            db.session.commit()
            return {"message": "New interest created"}, 201
        except ValueError as e:
            return {"error": [str(e)]}
    