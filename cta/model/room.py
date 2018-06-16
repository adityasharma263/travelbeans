# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Room(Base):
    __tablename__ = 'room'

    image = db.Column(db.String, nullable=True)
    room_type = db.Column(db.Integer, nullable=True)
    bed_type = db.Column(db.Integer, nullable=True)
    no_of_bed = db.Column(db.Integer, nullable=True)
    check_in = db.Column(db.DateTime(timezone=True), nullable=False)
    check_out = db.Column(db.DateTime(timezone=True), nullable=False)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
    member = db.relationship('Member', uselist=False, backref='room')
    facilities = db.relationship('Facility', uselist=False, backref='room')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<room_type %r>' % self.room_type


class Member(Base):
    __tablename__ = 'member'

    no_of_adults = db.Column(db.Integer, nullable=True)
    no_of_children = db.Column(db.Integer, nullable=True)
    total_members = db.Column(db.Integer, nullable=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<total_members %r>' % self.total_members


class Facility(Base):
    __tablename__ = 'facility'

    bathroom_with_shower = db.Column(db.Boolean, default=False, nullable=True)
    bathroom_nightie = db.Column(db.Boolean, default=False, nullable=True)
    wardrobes_closet = db.Column(db.Boolean, default=False, nullable=True)
    room_slipper = db.Column(db.Boolean, default=False, nullable=True)
    morning_newspaper = db.Column(db.Boolean, default=False, nullable=True)
    food_serve_at_room = db.Column(db.Boolean, default=False, nullable=True)
    ironing_facility = db.Column(db.Boolean, default=False, nullable=True)
    view = db.Column(db.Boolean, default=False, nullable=True)
    free_toiletries = db.Column(db.Boolean, default=False, nullable=True)
    bathroom_towels = db.Column(db.Boolean, default=False, nullable=True)
    bathroom_cosmetics = db.Column(db.Boolean, default=False, nullable=True)
    weighing_machine = db.Column(db.Boolean, default=False, nullable=True)
    room_seating_area = db.Column(db.Boolean, default=False, nullable=True)
    room_slippers = db.Column(db.Boolean, default=False, nullable=True)
    free_evening_snacks = db.Column(db.Boolean, default=False, nullable=True)
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
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<ac %r>' % self.ac
