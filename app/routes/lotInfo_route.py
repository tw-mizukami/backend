import pdb
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError, post_load
from app.models.lot_model import BoxNum, LotInfo
from app.schemas.lot_shema import LotInfoSchema
from app.extensions import db

lotInfo_route = Blueprint("lotInfo_route", __name__)

@lotInfo_route.route("/lotInfo", methods=["POST"])
def create_lot_info():
    json_data = request.get_json()
    print(f"Received JSON data: {json_data}")
    print(f"Data type: {type(json_data)}")

    schema = LotInfoSchema()
    
    try:
        # JSONデータをロードして、辞書形式のデータを得る
        data = schema.load(json_data)

        # データが辞書形式であることを確認
        if isinstance(data, dict):
            # LotInfoインスタンスを作成
            lot_info_instance = LotInfo(
                start_time=data.get('start_time'),
                productionPlan_num=data.get('productionPlan_num'),
                supply_num=data.get('supply_num'),
            )

            for box_data in data.get('box_num', []):
                box_num_instance = BoxNum(num=box_data['num'])
                lot_info_instance.box_num.append(box_num_instance)

            db.session.add(lot_info_instance)
            db.session.commit()

            return jsonify(schema.dump(lot_info_instance)), 201
        else:
            return jsonify({"error": "Invalid data format"}), 400

    except ValidationError as ve:
        print(f"Validation Error: {ve.messages}")
        return jsonify({"error": "Validation error", "messages": ve.messages}), 400
    except Exception as e:
        import traceback
        print(f"Unexpected Error: {str(e)}")
        traceback.print_exc()  # トレースバックを表示
        return jsonify({"error": "An unexpected error occurred"}), 500
