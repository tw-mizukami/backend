from flask import Blueprint, request, jsonify

machineInfo_route = Blueprint("machineInfo_route", __name__)

@machineInfo_route.route("/machineInfo", methods=["GET"])

# PLCからIPアドレスをもらい、装置情報を取得
# ソフト起動時は、登録されている装置全ての情報を取得
def get_machines():
    return jsonify({
        # 一旦、仮で固定値を送る
        "Machine1":["192.168.0.10", "1000", "2000", "3000"],
        "Machine2":["192.168.0.11", "2000", "3000", "4000"],
        "Machine3":["192.168.0.12", "3000", "4000", "5000"],
        "Machine4":["192.168.0.13", "4000", "5000", "6000"],
        "Machine5":["192.168.0.13", "4000", "5000", "6000"]
    })
    