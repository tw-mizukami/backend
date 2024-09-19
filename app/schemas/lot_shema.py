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

    @pre_load
    def preprocess_box_num(self, data, **kwargs):
     # 辞書形式であるか確認
        if isinstance(data, dict):
            # box_numのリストが整数の場合、辞書のリストに変換
            if  'box_num' in data and isinstance(data['box_num'], list):
                print("Before conversion:", data['box_num'])  # 追加
                data['box_num'] = [{'num': num} for num in data['box_num']]
                print("After conversion:", data['box_num'])  # 追加
        
        return data
