from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
    stores_obj = db.relationship("StoreModel", back_populates="items_obj")
    tags_obj = db.relationship("TagModel", back_populates="items_obj", secondary="items_tags")