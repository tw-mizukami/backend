from app.extensions import db
from sqlalchemy.dialects.postgresql import ARRAY

class LotInfo(db.Model):
    __tablename__ = "lot_info"

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    start_time = db.Column(db.DateTime, nullable=False)
    productionPlan_num = db.Column(db.Integer, nullable=False)
    supply_num = db.Column(db.Integer, nullable=False)
    box_num = db.Column(ARRAY(db.Integer), nullable=False)

