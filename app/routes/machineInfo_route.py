import pdb

from flask import Blueprint, request, jsonify
from app.models.machine_model import MachineInfo
from app.schemas.machine_shema import MachineInfoSchema
from app.extensions import db
from marshmallow import ValidationError

machineInfo_route = Blueprint("machineInfo_route", __name__)

@machineInfo_route.route("/machineInfo", methods=["DELETE"])
def delete_machines():
    machine_infos = MachineInfo.query.all()
    
    # 全てのデータを削除
    for machine_info in machine_infos:
        db.session.delete(machine_info)
    
    # コミットして削除を確定
    db.session.commit()
    
    return jsonify("All machine records deleted successfully.")

# FrontEndからIPアドレスをもらい、そのIPアドレスの装置情報を取得
# ソフト起動時は、登録されている装置全ての情報を取得
@machineInfo_route.route("/machineInfo", methods=["GET"])
def get_machines():
    machine_infos = MachineInfo.query.all()
    return jsonify(MachineInfoSchema(many=True).dump(machine_infos))

# ipアドレスを受け取る。そのIPアドレスに接続されている設備があれば、装置情報を取得して返す。
@machineInfo_route.route("/machineInfo", methods=["POST"])
def create_machine_info():
    json_data = request.get_json()
    print(f"Received JSON data: {json_data}")
    print(f"Data type: {type(json_data)}")
    
    # データの型をチェック
    if isinstance(json_data, list):
        # 複数のオブジェクトを処理
        schema = MachineInfoSchema(many=True)
        try:
            objects = schema.load(json_data)
            db.session.bulk_save_objects(objects)
            db.session.commit()
            return jsonify(schema.dump(objects)), 201
        except ValidationError as e:
            print(f"Validation Error: {e.messages}")
            return jsonify(e.messages), 422
        except Exception as e:
            print(f"Unexpected Error: {str(e)}")
            return jsonify({"error": "An unexpected error occurred"}), 500

    elif isinstance(json_data, dict):
        # 単一のオブジェクトを処理
        schema = MachineInfoSchema()
        try:
            obj = schema.load(json_data)
            db.session.add(obj)
            db.session.commit()
            return jsonify(schema.dump(obj)), 201
        except ValidationError as e:
            print(f"Validation Error: {e.messages}")
            return jsonify(e.messages), 422
        except Exception as e:
            print(f"Unexpected Error: {str(e)}")
            return jsonify({"error": "An unexpected error occurred"}), 500

    else:
        return jsonify({"error": "Invalid JSON data. Expected a dictionary or list."}), 400
        




    