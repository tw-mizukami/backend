from flask import Blueprint, request, jsonify

machineInfo_route = Blueprint("machineInfo_route", __name__)

@machineInfo_route.route("/machineInfo", methods=["GET"])
def get_machines():
    return jsonify({
        "Machine1":["192.168.0.10", "1000", "2000", "3000"],
        "Machine2":["192.168.0.11", "2000", "3000", "4000"],
        "Machine2":["192.168.0.12", "3000", "4000", "5000"]
    })
    