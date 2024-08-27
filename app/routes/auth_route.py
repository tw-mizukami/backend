from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from app.models.user_model import User
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

@auth_router.route("/user/login", methods=["POST"])
def login():
   data = request.get_json()
   print(data)

   user = User.query.filter_by(username=data["username"]).first()

   if not user:
      return jsonify({"message":"ユーザー名またはパスワードが間違っています。"}), 401
   
   is_corrected = check_password_hash(user.password, data["password"])

   if not is_corrected:
      return jsonify({"message":"ユーザー名またはパスワードが間違っています。"}), 401
   
   access_token = create_access_token(identity=user.id)

   return jsonify({"access_token": access_token}), 200