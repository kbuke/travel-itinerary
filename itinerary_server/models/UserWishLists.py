from sqlalchemy import func
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from config import db

class UserWishListModel(db.Model, SerializerMixin):
    __tablename__ = "user_wishlists"

    id = db.Column(db.Integer, primary_key = True)
    wishlist_name = db.Column(db.String, nullable = False)

    # RELATIONS
    user_id = db.Column(db.ForeignKey("users.id"), nullable = False)
    user = db.relationship("UserModel", back_populates = "wishlists")

    sites = db.relationship("SitesModel", back_populates = "wishlists", secondary = "site_wishlists")

    serialize_rules = (
        "-user.wishlists",
    )

    @validates("wishlist_name", "user_id")
    def validate_wishlist(self, key, value):
        if key == "wishlist_name" and (not isinstance(value, str) or value == ""):
            raise ValueError("Please enter a valid wishlist name")
        
        wishlist_name = value if key == "wishlist_name" else self.wishlist_name
        user_id = value if key == "user_id" else self.user_id
        
        existing_user_wishlist = UserWishListModel.query.filter(
            func.lower(UserWishListModel.wishlist_name)==wishlist_name.lower(),
            UserWishListModel.user_id == user_id
        ).first()

        if existing_user_wishlist and existing_user_wishlist.id != self.id:
            raise ValueError(f"Wishlist already created by this user")
        
        return value