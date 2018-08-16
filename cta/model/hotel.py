# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base
# import enum
#
# class HotelCategory(enum.Enum):
#     1 = "Crunchy apple"
#     BANANA = "Sweet banana


class Hotel(Base):
    __tablename__ = 'hotel'

    name = db.Column(db.String)
    star = db.Column(db.Integer, nullable=True)
    is_partner = db.Column(db.Boolean, default=False, nullable=True)
    rating = db.Column(db.DECIMAL, nullable=True)
    phone = db.Column(db.String, nullable=True, unique=True)
    city = db.Column(db.String, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    category = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String, nullable=True)
    images = db.relationship('Image', backref='hotel')
    rooms = db.relationship('Room', backref='hotel')
    collection = db.relationship('HotelCollection', uselist=False)
    latitude = db.Column('latitude', db.Float(asdecimal=True), nullable=True)
    longitude = db.Column('longitude', db.Float(asdecimal=True), nullable=True)
    amenities = db.relationship('Amenity', uselist=False, backref='hotel')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<name %r>' % self.name


class HotelCollection(Base):
    __tablename__ = 'hotel_collection'

    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), unique=True, nullable=True)
    collection_name = db.Column(db.String, nullable=True)
    featured = db.Column(db.Boolean, default=False, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    image = db.Column(db.String, nullable=True)
    products = db.relationship('CollectionProduct', backref='hotel_collection')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<collection %r>' % self.collection


class CollectionProduct(Base):
    __tablename__ = 'collection_product'

    hotel_collection_id = db.Column(db.Integer, db.ForeignKey('hotel_collection.id'), nullable=False)
    product_url = db.Column(db.String, nullable=True)
    product_name = db.Column(db.String, nullable=True)
    featured_product = db.Column(db.Boolean, default=False, nullable=True)
    product_desc = db.Column(db.Text, nullable=True)
    product_image = db.Column(db.String, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<image_url %r>' % self.image_url


class Room(Base):
    __tablename__ = 'room'

    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=True)
    room_type = db.Column(db.Integer, nullable=True)
    image_url = db.Column(db.String, nullable=True)
    other_room_type = db.Column(db.String, nullable=True)
    check_in = db.Column(db.DateTime(timezone=True), nullable=True)
    check_out = db.Column(db.DateTime(timezone=True), nullable=True)
    breakfast = db.Column(db.Boolean, default=False, nullable=True)
    balcony = db.Column(db.Boolean, default=False, nullable=True)
    member = db.relationship('Member', uselist=False, backref='room')
    facilities = db.relationship('Facility', uselist=False, backref='room')
    deals = db.relationship('Deal', backref='room')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<hotel_id %r>' % self.hotel_id



class Amenity(Base):
    __tablename__ = 'amenity'
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), unique=True, nullable=False)
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


class Image(Base):
    __tablename__ = 'image'
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), nullable=False)
    image_url = db.Column(db.String, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<image_url %r>' % self.image_url



class Member(Base):
    __tablename__ = 'member'

    no_of_adults = db.Column(db.Integer, nullable=True)
    children = db.Column(db.Integer, nullable=True)
    total_members = db.Column(db.Integer, nullable=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), unique=True, nullable=False)

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
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), unique=True, nullable=False)

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
    weekend = db.Column(db.Boolean, default=False, nullable=False)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'), unique=False, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), unique=False, nullable=False)
    website = db.relationship('Website', foreign_keys=website_id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<room_id %r>' % self.room_id


