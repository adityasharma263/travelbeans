# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Price(Base):
    __tablename__ = 'price'

    price = db.Column(db.Integer, nullable=True)
    avg_price = db.Column(db.Integer, nullable=True)
    website_room_id = db.Column(db.Integer, db.ForeignKey("website_room.website_room_id"))
    # website_id = db.Column(db.Integer)
    # website_room_id = db.Column(db.Integer)
    # fk_website_room_id = db.ForeignKeyConstraint([website_id, website_room_id], ['website_room.website_id', 'website_room.id'])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<price %r>' % self.price