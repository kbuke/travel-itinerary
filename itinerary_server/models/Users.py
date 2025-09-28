from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt

class UserModel(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = True)
    _password_hash = db.Column(db.String, nullable = False)
    user_img = db.Column(db.String, nullable = False)
    gender = db.Column(db.String, nullable = False)
    is_private = db.Column(db.Boolean, nullable = False)

    # HASH PASSWORD
    @hybrid_property
    def password_hash(self):
        raise AttributeError("password: write-only attribute")
    
    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)

    # VALIDATIONS
    @validates("username")
    def validate_username(self, key, value):
        # 1 - Ensure username is a string
        if not isinstance(value, str) or value == "":
            raise ValueError("Please enter a valid username")
        
        # 2 - Ensure username is not already registered
        existing_username = UserModel.query.filter(UserModel.username == value).first()
        if existing_username and existing_username.id != self.id:
            raise ValueError(f"{value} is already registered on this account.")
        
        return value
    
    @validates("user_img", "gender")
    def validate_img_gender(self, key, value):
        # 1 - Ensure gender is defined as one of the options
        available_options = ["Male", "Female", "Other"]

        if key == "gender" and value.capitalize() not in available_options:
            raise ValueError("Gender must be either Male, Female or Other")
                
        # 2 - If no profile picture set an avatar based on gender
        if key == "user_img" and (value is None or value == ""):
            if self.gender == "Male":
                value = "https://static.vecteezy.com/system/resources/previews/024/183/525/non_2x/avatar-of-a-man-portrait-of-a-young-guy-illustration-of-male-character-in-modern-color-style-vector.jpg"
            elif self.gender == "Female":
                value = "https://t4.ftcdn.net/jpg/11/66/06/77/360_F_1166067709_2SooAuPWXp20XkGev7oOT7nuK1VThCsN.jpg"
            else:
                value = "https://img.freepik.com/free-photo/androgynous-avatar-non-binary-queer-person_23-2151100270.jpg"
        
        return value
