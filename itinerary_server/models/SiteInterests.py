from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

class SiteInterestsModel(db.Model, SerializerMixin):
    __tablename__ = "site_interests"

    id = db.Column(db.Integer, primary_key = True)
    site_id = db.Column(db.ForeignKey("sites.id"))
    interest_id = db.Column(db.ForeignKey("interests.id"))