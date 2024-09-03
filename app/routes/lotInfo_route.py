import pdb

from flask import Blueprint, request, jsonify
from app.models.lot_model import LotInfo
from app.schemas.lot_shema import LotInfoSchema
from app.extensions import db

lotInfo_route = Blueprint("lotInfo_route", __name__)

@lotInfo_route.route("/lotInfo", methods=["POST"])
def create_lot_info():
    json_data = request.get_json()
    print(f"Received JSON data: {json_data}")
    print(f"Data type: {type(json_data)}")

    # idまたはIPアドレスを受け取り、装置からlotInfoデータを取得して返す
    
    schema = LotInfoSchema()
    try:
        data = schema.load(json_data)

        lot_info = LotInfo(
            start_time= "2024/12/12 12:12:12",
            productionPlan_num="1000",
            supply_num="1000",
            box_num="1000,1000,1000",
        )

        db.session.add(lot_info)
        db.session.commit()
        return jsonify(schema.dump(lot_info)), 201
   
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500
    