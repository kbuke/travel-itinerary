from models.UserWishLists import UserWishListModel
from config import db 

from flask import request
from flask_restful import Resource

class UserWishlistList(Resource):
    def get(self):
        wishlists = [wishlist.to_dict() for wishlist in UserWishListModel.query.all()]
        return wishlists, 200
    
    def post(self):
        json = request.get_json()
        try:
            new_wishlist = UserWishListModel(
                wishlist_name = json.get("wishlistName"),
                user_id = json.get("userId")
            )
            db.session.add(new_wishlist)
            db.session.commit()
            return {"message": "New wishlist created"}
        except ValueError as e:
            return {"error": [str(e)]}