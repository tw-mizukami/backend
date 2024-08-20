from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from app.schemas.user_schema import UserSchema
from app.extensions import db

auth_router = Blueprint('auth', __name__)

@auth_router.route("/user/register", methods=["POST"])

def register():
   data = request.get_json()

   # バリテーション処理
   schema = UserSchema()
   errors = schema.validate(data)

   if errors:
    return jsonify(errors), 400

    # パスワードのハッシュ化
   hashed_password = generate_password_hash(data["password"])

    # 登録処理
   data["password"] = hashed_password
   new_user = schema.load(data)
   db.session.add(new_user)
   db.session.commit()

    # リターン
   return schema.jsonify(new_user), 201

    