# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Hotel(Base):
    __tablename__ = 'hotel'

    name = db.Column(db.String)
    star = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    status = db.Column(db.Boolean, default=False, nullable=True)
    city = db.Column(db.String, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    address = db.Column(db.String, nullable=True)
    room_type = db.Column(db.Integer, nullable=True)
    check_in = db.Column(db.DateTime(timezone=True), nullable=False)
    check_out = db.Column(db.DateTime(timezone=True), nullable=False)
    breakfast = db.Column(db.Boolean, default=False, nullable=True)
    balcony = db.Column(db.Boolean, default=False, nullable=True)
    member = db.relationship('Member', uselist=False, backref='hotel')
    facilities = db.relationship('Facility', uselist=False, backref='hotel')
    deals = db.relationship('Deal', backref='hotel')
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    images = db.relationship('Image', foreign_keys=image_id)
    amenity_id = db.Column(db.Integer, db.ForeignKey('amenity.id'))
    Amenities = db.relationship('Amenity', foreign_keys=amenity_id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<name %r>' % self.name


class Image(Base):
    __tablename__ = 'image'

    image_url = db.Column(db.String, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<image_url %r>' % self.image_url

class Amenity(Base):
    __tablename__ = 'amenity'

    conference_room = db.Column(db.Boolean, default=False, nullable=True)
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

class Member(Base):
    __tablename__ = 'member'

    no_of_adults = db.Column(db.Integer, nullable=True)
    children = db.Column(db.Integer, nullable=True)
    total_members = db.Column(db.Integer, nullable=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<total_members %r>' % self.total_members


class Facility(Base):
    __tablename__ = 'facility'

    bed_type = db.Column(db.Integer, nullable=True)
    no_of_bed = db.Column(db.Integer, nullable=True)
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
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<ac %r>' % self.ac


class Website(Base):
    __tablename__ = 'website'

    website = db.Column(db.String)
    logo_image = db.Column(db.String, nullable=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<website %r>' % self.website


class Deal(Base):
    __tablename__ = 'deal'

    price = db.Column(db.Integer, nullable=True)
    hotel_url = db.Column(db.String)
    weekend = db.Column(db.Boolean, default=False,nullable=False)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), unique=False)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'), unique=False)
    website = db.relationship('Website', foreign_keys=website_id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<price %r>' % self.price