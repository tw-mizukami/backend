from app.extensions import db

class MachineInfo(db.Model):
    __tablename__ = "machine_info"

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    ip = db.Column(db.String(40), nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    good_num = db.Column(db.Integer, nullable=False)
    ng_num = db.Column(db.Integer, nullable=False)