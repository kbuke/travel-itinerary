from sqlalchemy import func
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from config import db 

from models.Country import CountryModel

class CityModel(db.Model, SerializerMixin):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key = True)
    city_name = db.Column(db.String, nullable = False)
    city_img = db.Column(db.String, nullable = False)
    city_intro = db.Column(db.String, nullable = False)
    population = db.Column(db.String, nullable = False)

    # RELATIONS
    country_id = db.Column(db.ForeignKey("countries.id"))
    country = db.relationship("CountryModel", back_populates = "cities")

    sites = db.relationship("SitesModel", back_populates = "city")

    # SERIALIZE RULES
    serialize_rules = (
        "-country.cities",
        "-country.sites",

        "-sites.city",
        "-sites.country",
    )

    # VALIDATIONS
    @validates("population")
    def validate_population(self, key, value):
        # 1 - Convert inputted population to a integer
        try:
            population_int = int(value)
        except ValueError:
            raise ValueError("Population must be a valid integer")

        # 2 - Check the value is an integer and has a poplulaton of at least a thousand and less than 50million
        if population_int < 1000 or 50_000_000 < population_int:
            raise ValueError("Value must be an integer greater than a thousand, and less than 50million")
        
        # 3 - Tidy up population size if number is between one-thousan and nine-hundred-and-ninety-nine-thousand
        if 1_000 <= population_int <= 999_999:
            population_int = round(population_int / 1_000, 2)
            return f"{str(population_int)} Thousand"
        
        # 4 - Tidy up population size if number is between 1_000_000 and 50_000_000
        if 1_000_000 <= population_int <= 50_000_000:
            population_int = round(population_int / 1_000_000, 2)
            return f"{str(population_int)} Million"
    
    @validates("city_name", "country_id")
    def validate_city(self, key, value):
        # 1 - check a string-value has been given of city_name
        if key == "city_name":
            if not isinstance(value, str) or value == "":
                raise ValueError("Please enter a valid city name")
        
        # 2 - check the country is registered on app
        if key == "country_id":
            existing_country = CountryModel.query.filter(CountryModel.id == value).first()
            if not existing_country:
                raise ValueError(f"Country {value} is not registered on the application.")
        
        # 3 - check if the city is registered with the country already
        city_name = value if key == "city_name" else self.city_name
        country_id = value if key == "country_id" else self.country_id

        existing_city_country = CityModel.query.filter(
            func.lower(CityModel.city_name)==city_name.lower(),
            CityModel.country_id==country_id
        ).first()

        if existing_city_country and existing_city_country.id != self.id:
            raise ValueError(f"{city_name} is already registered with country {country_id}")
        
        return value


    