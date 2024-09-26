from app.extensions import db
from sqlalchemy.dialects.mysql import JSON

class LotInfo(db.Model):
    __tablename__ = "lot_info"

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    start_time = db.Column(db.String, nullable=False)
    productionPlan_num = db.Column(db.Integer, nullable=False)
    supply_num = db.Column(db.Integer, nullable=False)
    # box_nums = db.relationship('BoxNum', backref='lot_info', lazy=True)

class BoxNum(db.Model):
    __tablename__ = "box_num"

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    num = db.Column(db.Integer, nullable=False)

    lot_info_id = db.Column(db.Integer, db.ForeignKey('lot_info.id'), nullable=False)

    lot_info = db.relationship("LotInfo")
