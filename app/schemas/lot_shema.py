from app.extensions import ma
from app.models.lot_model import BoxNum, LotInfo
from marshmallow import fields, pre_load

class BoxNumSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BoxNum
        load_instance = True

    num = fields.Integer(required=True)
    lot_info = fields.Integer(dump_only=True)

class LotInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LotInfo
        load_instance = True

    start_time = fields.String(required=True)
    productionPlan_num = fields.Integer(required=True)
    supply_num = fields.Integer(required=True)
    box_num = fields.List(fields.Nested(BoxNumSchema), required=False)

