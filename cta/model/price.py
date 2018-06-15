# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Price(Base):
    __tablename__ = 'price'

    price = db.Column(db.Integer, nullable=True)
    avg_price = db.Column(db.Integer, nullable=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<our_price %r>' % self.our_price