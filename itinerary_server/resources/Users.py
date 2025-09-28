from models.Users import UserModel

from flask import request
from flask_restful import Resource

from config import db

class UserList(Resource):
    def get(self):
        users = [user.to_dict() for user in UserModel.query.all()]
        return users, 200
    
    def post(self):
        json = request.get_json()
        try:
            new_user = UserModel(
                username = json.get("username"),
                user_img = json.get("userImg"),
                gender = json.get("gender"),
                is_private = json.get("isPrivate")
            )
            new_user.password_hash = json.get("password")
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"New User created."}, 201
        except ValueError as e:
            return {"error": [str(e)]}, 401