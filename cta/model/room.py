# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Room(Base):
    __tablename__ = 'room'

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
    hotels = db.relationship('Hotel', backref='room')
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    members = db.relationship('Member', foreign_keys=member_id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<room_type %r>' % self.room_type