from flask import Blueprint, request, jsonify

machines_route = Blueprint("machines_route", __name__)

@machines_route.route("/machines", methods=["GET"])
def get_machines():
    return jsonify({"message":"OK"})
    