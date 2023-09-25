from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    items_obj = db.relationship("ItemModel", back_populates="stores_obj", lazy="dynamic", cascade="all, delete")
    tags_obj = db.relationship("TagModel", back_populates="stores_obj", lazy="dynamic")