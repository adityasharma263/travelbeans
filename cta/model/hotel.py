# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Hotel(Base):
    __tablename__ = 'hotel'

    name = db.Column(db.String)
    star = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    city = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'))
    websites = db.relationship('Website', foreign_keys=website_id)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    images = db.relationship('Image', foreign_keys=image_id)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    rooms = db.relationship('Room', foreign_keys=room_id)
    amenity_id = db.Column(db.Integer, db.ForeignKey('amenity.id'))
    amenities = db.relationship('Amenity', foreign_keys=amenity_id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<name %r>' % self.name