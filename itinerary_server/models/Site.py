from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from config import db
from models.Country import CountryModel

class SitesModel(db.Model, SerializerMixin):
    __tablename__ = "sites"

    id = db.Column(db.Integer, primary_key = True)
    site_name = db.Column(db.String, nullable = False, unique = True)
    site_img = db.Column(db.String, nullable = False)
    address_line_1 = db.Column(db.String, nullable = False)
    address_line_2 = db.Column(db.String, nullable = True)
    address_line_3 = db.Column(db.String, nullable = True)
    post_code = db.Column(db.String, nullable = False)

    # RELATIONSHIPS
    country_id = db.Column(db.ForeignKey("countries.id"))
    country = db.relationship("CountryModel", back_populates = "sites")

    interests = db.relationship("InterestsModel", back_populates = "sites", secondary = "site_interests")

    # SERIALIZE RULES
    serialize_rules = (
        "-country.sites",
    )

    # VALIDATES
    @validates("country_id", "site_name")
    def validate_country(self, key, value):
        # 1 - Ensure country exists
        if key == "country_id":
            existing_country = CountryModel.query.filter(CountryModel.id == value).first()
            if not existing_country:
                raise ValueError(f"Country {value} does not exist.")
        
        # 2 - Ensure site name is a string, but not an empty one
        if key == "site_name":
            if not isinstance(value, str) or value == "":
                raise ValueError("Please enter a valid site name")
            
            # 3 - Ensure the site is not registered on the application
            existing_site = SitesModel.query.filter(SitesModel.site_name == value).first()
            if existing_site and existing_site.id != self.id:
                raise ValueError(f"{value} is already registered on this app.")
        
        return value
        
      
