# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Price(Base):
    __tablename__ = 'price'

    price = db.Column(db.Integer, nullable=True)
    avg_price = db.Column(db.Integer, nullable=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), unique=False)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'), unique=False)
    room = db.relationship('Room', foreign_keys=room_id)
    website = db.relationship('Website', foreign_keys=website_id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<price %r>' % self.price