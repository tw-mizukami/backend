from app.extensions import ma
from app.models.lot_model import LotInfo
from marshmallow import fields

class LotInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LotInfo
        load_instance = True  # インスタンスを返すために必要です

    start_time = fields.String(required=True)
    productionPlan_num = fields.String(required=True)  
    supply_num = fields.String(required=True)  
    box_num = fields.String( required=True)