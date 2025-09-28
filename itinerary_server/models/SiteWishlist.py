from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from config import db 

class SiteWishlistModel(db.Model, SerializerMixin):
    __tablename__ = "site_wishlists"

    id = db.Column(db.Integer, primary_key = True)

    # RELATIONS
    site_id = db.Column(db.ForeignKey("sites.id"))
    
    wishlist_id = db.Column(db.ForeignKey("user_wishlists.id"))