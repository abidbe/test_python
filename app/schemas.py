from app import ma
from app.models import Data, User
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class DataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Data
        load_instance = True

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

data_schema = DataSchema()
datas_schema = DataSchema(many=True)
user_schema = UserSchema()  # Tambahkan definisi ini jika diperlukan
