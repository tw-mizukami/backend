# from flask import Blueprint, request, jsonify

# machineInfo_route = Blueprint("machineInfo_route", __name__)

# @machineInfo_route.route("/machineInfo", methods=["GET"])

# # PLCからIPアドレスをもらい、装置情報を取得
# # ソフト起動時は、登録されている装置全ての情報を取得
# def get_machines():
#     return jsonify({
#         # 一旦、仮で固定値を送る
#         "Machine1":["192.168.0.10", "1000", "2000", "3000"],
#         "Machine2":["192.168.0.11", "2000", "3000", "4000"],
#         "Machine3":["192.168.0.12", "3000", "4000", "5000"],
#         "Machine4":["192.168.0.13", "4000", "5000", "6000"],
#         "Machine5":["192.168.0.13", "4000", "5000", "6000"]
#     })

from flask import Blueprint, request, jsonify
from app.models.machine_model import MachineInfo
from app.schemas.machine_shema import MachineInfoSchema
from app import db  # dbのインポートを確認してください
from marshmallow import ValidationError  # ValidationErrorのインポートを確認してください

machineInfo_route = Blueprint("machineInfo_route", __name__)

# FrontEndからIPアドレスをもらい、そのIPアドレスの装置情報を取得
# ソフト起動時は、登録されている装置全ての情報を取得
@machineInfo_route.route("/machineInfo", methods=["GET"])
def get_machines():
    machine_infos = MachineInfo.query.all()
    return jsonify(MachineInfoSchema(many=True).dump(machine_infos))

@machineInfo_route.route("/machineInfo", methods=["POST"])
def create_machine_info():
    json = request.get_json()  # request.json() ではなく、request.get_json() を使用します
    
    schema = MachineInfoSchema()
    
    try:
        data = schema.load(json)
        db.session.add(data)
        db.session.commit()
        return jsonify(data), 201
    except ValidationError as e:
        return jsonify(e.messages), 422

        




    