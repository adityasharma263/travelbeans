# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Room(Base):
    __tablename__ = 'room'

    images = db.Column(db.String, nullable=True)
    room_type = db.Column(db.Integer, nullable=True)
    bed_type = db.Column(db.Integer, nullable=True)
    no_of_bed = db.Column(db.Integer, nullable=True)
    check_in = db.Column(db.DateTime(timezone=True), nullable=False)
    check_out = db.Column(db.DateTime(timezone=True), nullable=False)
    ac = db.Column(db.Boolean, default=False, nullable=True)
    hairdryer = db.Column(db.Boolean, default=False, nullable=True)
    wifi = db.Column(db.Boolean, default=False, nullable=True)
    tv = db.Column(db.Boolean, default=False, nullable=True)
    phone = db.Column(db.Boolean, default=False, nullable=True)
    room_safe = db.Column(db.Boolean, default=False, nullable=True)
    heater = db.Column(db.Boolean, default=False, nullable=True)
    desk = db.Column(db.Boolean, default=False, nullable=True)
    fan = db.Column(db.Boolean, default=False, nullable=True)
    electric_kettle = db.Column(db.Boolean, default=False, nullable=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
    members = db.relationship('Member', backref='room')
    websites = db.relationship('Website', backref='room')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<room_type %r>' % self.room_type