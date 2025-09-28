from models.SiteWishlist import SiteWishlistModel

from config import db 

from flask import request
from flask_restful import Resource

class SiteWishlistList(Resource):
    def get(self):
        wishlists = [wishlist.to_dict() for wishlist in SiteWishlistModel.query.all()]
        return wishlists, 200