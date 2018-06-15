# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Hotel(Base):
    __tablename__ = 'hotel'

    name = db.Column(db.String)
    images = db.Column(db.String, nullable=True)
    star = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    city = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    rooms = db.relationship('Room', backref='hotel')
    amenities = db.relationship('Amenity', uselist=False, backref='hotel')
    websites = db.relationship('WebsiteHotel', backref="hotel")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<name %r>' % self.name