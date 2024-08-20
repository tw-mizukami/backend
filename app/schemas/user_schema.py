from marshmallow import validates, ValidationError, fields

from app.extensions import ma
from app.models.user_model import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    password = fields.String(load_only=True, required=True)

    class Meta:
        model = User
        load_instance = True
        #exclude = ("id")

    @validates("username")
    def validate_username(self, username):
        print("validate")
        if len(username) < 4:
            raise ValidationError("ユーザー名を4文字以上で入力してください")