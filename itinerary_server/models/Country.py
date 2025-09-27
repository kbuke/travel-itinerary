from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from config import db

class CountryModel(db.Model, SerializerMixin):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key = True)
    country_name = db.Column(db.String, nullable = False, unique = True)
    country_img = db.Column(db.String, nullable = False)
    country_intro = db.Column(db.String, nullable = False)

    @validates("country_name")
    def validate_country(self, key, value):
        # 1 - check value exists and is a string
        if not isinstance(value, str) or value == "":
            raise ValueError("Country name must be of type string and can not be an empty string.")
        
        # 2 - ensure country is not already registered
        exisiting_country = CountryModel.query.filter(CountryModel.country_name == value).first()
        if exisiting_country and exisiting_country.id != self.id:
            raise ValueError(f"{value} is already registered on this application.")
        
        return value