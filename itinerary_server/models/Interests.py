from config import db 
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

class InterestsModel(db.Model, SerializerMixin):
    __tablename__ = "interests"

    id = db.Column(db.Integer, primary_key = True)
    interest = db.Column(db.String, nullable = False, unique = True)
    interest_img = db.Column(db.String, nullable = False)

    # RELATIONS
    sites = db.relationship("SitesModel", back_populates = "interests", secondary = "site_interests")

    # SERIALIZE RULES
    serialize_rules = (
        "-sites.interests",
    )

    @validates("interest")
    def validate_interest(self, key, value):
        # 1 - Ensure interest is a string, and not an empty one
        if not isinstance(value, str) or value == "":
            raise ValueError("Please enter a valid interest")
        
        # 2 - Ensure this interest has not already been registered
        existing_interest = InterestsModel.query.filter(InterestsModel.interest == value).first()
        if existing_interest and existing_interest.id != self.id:
            raise ValueError(f"{value} is already registered as an interest on this app.")
        
        return value
    
    @validates("interest_img")
    def validate_img(self, key, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("Please enter a proper string for the interests image")
        
        return value