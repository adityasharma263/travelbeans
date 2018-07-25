# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Cab(Base):
    __tablename__ = 'cab'

    name = db.Column(db.String)
    star = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    city = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    address = db.Column(db.String, nullable=True)
    images = db.relationship('Image', backref='hotel')
    rooms = db.relationship('Room', backref='hotel')
    latitude = db.Column('latitude', db.Float(asdecimal=True), nullable=True)
    longitude = db.Column('longitude', db.Float(asdecimal=True), nullable=True)
    amenities = db.relationship('Amenity', uselist=False, backref='hotel')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<name %r>' % self.name


class CabImage(Base):
    __tablename__ = 'cab_image'

    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
    image_url = db.Column(db.String, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<image_url %r>' % self.image_url


class CabAmenity(Base):
    __tablename__ = 'cab_amenity'

    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), unique=True)
    conference_room = db.Column(db.Boolean, default=False, nullable=True)
    parking = db.Column(db.Boolean, default=False, nullable=True)
    couple_friendly = db.Column(db.Boolean, default=False, nullable=True)
    express_check_in_out = db.Column(db.Boolean, default=False, nullable=True)
    laundry_service = db.Column(db.Boolean, default=False, nullable=True)
    indoor_swimming_pool = db.Column(db.Boolean, default=False, nullable=True)
    outdoor_swimming_pool = db.Column(db.Boolean, default=False, nullable=True)
    porter_service = db.Column(db.Boolean, default=False, nullable=True)
    Room_cleaning_service = db.Column(db.Boolean, default=False, nullable=True)
    terrace = db.Column(db.Boolean, default=False, nullable=True)
    child_baby_cot = db.Column(db.Boolean, default=False, nullable=True)
    wheelchair_accessible = db.Column(db.Boolean, default=False, nullable=True)
    doorman = db.Column(db.Boolean, default=False, nullable=True)
    hairdresser = db.Column(db.Boolean, default=False, nullable=True)
    banquets = db.Column(db.Boolean, default=False, nullable=True)
    non_smoking_smoking_rooms = db.Column(db.Boolean, default=False, nullable=True)
    pet_allowance = db.Column(db.Boolean, default=False, nullable=True)
    lift = db.Column(db.Boolean, default=False, nullable=True)
    bar = db.Column(db.Boolean, default=False, nullable=True)
    gym = db.Column(db.Boolean, default=False, nullable=True)
    pool = db.Column(db.Boolean, default=False, nullable=True)
    restaurant = db.Column(db.Boolean, default=False, nullable=True)
    spa = db.Column(db.Boolean, default=False, nullable=True)
    wifi_in_lobby = db.Column(db.Boolean, default=False, nullable=True)
    twenty_four_hr_reception = db.Column(db.Boolean, default=False, nullable=True)
    twenty_four_hr_room_service = db.Column(db.Boolean, default=False, nullable=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<pool %r>' % self.pool
