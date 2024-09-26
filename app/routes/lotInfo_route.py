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
        data = schema.load(json_data)

        lot_info_instance = LotInfo(
            start_time=json_data.get('start_time'),
            productionPlan_num=json_data.get('productionPlan_num'),
            supply_num=json_data.get('supply_num'),
        )
        
        db.session.add(lot_info_instance)
        db.session.commit()
        
        for box_data in json_data.get('box_num', []):
            box_num_instance = BoxNum(num=box_data['num'], lot_info=lot_info_instance)
            db.session.add(box_num_instance)
 
        db.session.commit()

        return jsonify(schema.dump(json_data)), 201

    except ValidationError as ve:
        print(f"Validation Error: {ve.messages}")
        db.session.rollback()
        return jsonify({"error": "Validation error", "messages": ve.messages}), 400
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        db.session.rollback()
        return jsonify({"error": "An unexpected error occurred"}), 500
    
    
    # PUT（全更新,PATCH（一部更新 更新処理
