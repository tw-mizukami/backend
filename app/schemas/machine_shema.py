from app.extensions import ma
from app.models.machine_model import MachineInfo
from marshmallow import fields, validate

class MachineInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MachineInfo
        load_instance = True  # インスタンスを返すために必要です

    ip = fields.String(
        validate=[
            validate.Length(min=1, max=40),
            validate.Regexp(
                r'^(\d{1,3}\.){3}\d{1,3}$',  # IPアドレスの基本的な形式を検証
                error='Invalid IP address format.'
            )
        ]
    )

    speed = fields.String(required=True)  
    good_num = fields.String(required=True)  
    ng_num = fields.String(required=True)  
