# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Cab(Base):
    __tablename__ = 'cab'

    car_name = db.Column(db.String)
    city = db.Column(db.String, nullable=True)
    rating = db.Column(db.DECIMAL, nullable=True)
    car_type = db.Column(db.Integer, nullable=True)
    cab_type = db.Column(db.Integer, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    deals = db.relationship('CabDeal', secondary='cab_deal_association')
    images = db.relationship('CabImage', backref='cab')
    collection_id = db.Column(db.Integer, db.ForeignKey('cab_collection.id'), nullable=True)
    amenities = db.relationship('CabAmenity', uselist=False, backref='cab')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<car_name %r>' % self.car_name

    def __hash__(self):
        return hash(self.name)


class CabCollection(Base):
    __tablename__ = 'cab_collection'

    collection_name = db.Column(db.String, nullable=True)
    featured = db.Column(db.Boolean, default=False, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    image = db.Column(db.String, nullable=True)
    products = db.relationship('CabCollectionProduct', backref='cab_collection')
    cabs = db.relationship('Cab', backref='cab_collection')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<collection %r>' % self.collection


class CabCollectionProduct(Base):
    __tablename__ = 'cab_collection_product'

    cab_collection_id = db.Column(db.Integer, db.ForeignKey('cab_collection.id'), nullable=False)
    product_url = db.Column(db.String, nullable=True)
    product_name = db.Column(db.String, nullable=True)
    featured_product = db.Column(db.Boolean, default=False, nullable=True)
    product_desc = db.Column(db.Text, nullable=True)
    product_image = db.Column(db.String, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<image_url %r>' % self.image_url



#
# class CabUser(Base):
#     __tablename__ = 'cab_user'
#
#     name = db.Column(db.String)
#     phone = db.Column(db.String, nullable=True, unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def __repr__(self):
#         return '<name %r>' % self.name
#
#
# class CabBooking(Base):
#     __tablename__ = 'cab_booking'
#
#     cab_booking_id = db.Column(db.String, nullable=True)
#     booking_date = db.Column(db.DateTime(timezone=True), nullable=True)
#     mode_of_payment = db.Column(db.Integer, nullable=True)
#     booking_status = db.Column(db.Integer, nullable=True)
#     pickup_time = db.Column(db.DateTime(timezone=True), nullable=False)
#     drop_time = db.Column(db.DateTime(timezone=True), nullable=False)
#     drop_latitude = db.Column('drop_latitude', db.Float(asdecimal=True), nullable=True)
#     drop_longitude = db.Column('drop_longitude', db.Float(asdecimal=True), nullable=True)
#     pickup_latitude = db.Column('pickup_latitude', db.Float(asdecimal=True), nullable=True)
#     pickup_longitude = db.Column('pickup_longitude', db.Float(asdecimal=True), nullable=True)
#     total_fare = db.Column(db.DECIMAL, nullable=True)
#     total_days = db.Column(db.Integer, nullable=True)
#     total_distance = db.Column(db.DECIMAL, nullable=True)
#     total_hours = db.Column(db.Integer, nullable=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('cab_user.id'))
#     cab_id = db.Column(db.Integer, db.ForeignKey('cab.id'))
#     deal_id = db.Column(db.Integer, db.ForeignKey('cab_deal.id'))
#     cab = db.relationship('Cab', foreign_keys=cab_id)
#     user = db.relationship('CabUser', foreign_keys=user_id)
#     deal = db.relationship('CabDeal', foreign_keys=deal_id)
#     tax = db.relationship('CabTax', uselist=False, backref='cab_booking')
#
#
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def __repr__(self):
#         return '<deal_id %r>' % self.deal_id


class CabImage(Base):
    __tablename__ = 'cab_image'

    cab_id = db.Column(db.Integer, db.ForeignKey('cab.id'))
    image_url = db.Column(db.String, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<image_url %r>' % self.image_url


class CabAmenity(Base):
    __tablename__ = 'cab_amenity'

    cab_id = db.Column(db.Integer, db.ForeignKey('cab.id'), unique=True)
    air_condition = db.Column(db.Boolean, default=False, nullable=True)
    seater = db.Column(db.Integer, nullable=True)
    baggage_allowance = db.Column(db.Boolean, default=False, nullable=True)
    doorstep_delivery = db.Column(db.Boolean, default=False, nullable=True)
    fuel = db.Column(db.Boolean, default=False, nullable=True)
    fuel_type = db.Column(db.Integer, nullable=True)
    fuel_capacity = db.Column(db.Integer, nullable=True)
    automatic = db.Column(db.Boolean, default=False, nullable=True)
    chauffeur = db.Column(db.Boolean, default=False, nullable=True)
    verified_driver = db.Column(db.Boolean, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<cab_id %r>' % self.cab_id


class CabWebsite(Base):
    __tablename__ = 'cab_website'

    website = db.Column(db.String)
    logo_image = db.Column(db.String, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<website %r>' % self.website


class CabDeal(Base):
    __tablename__ = 'cab_deal'

    website_id = db.Column(db.Integer, db.ForeignKey('cab_website.id'), unique=False)
    is_partner = db.Column(db.Boolean, default=False, nullable=True)
    cab_url = db.Column(db.String, nullable=True)
    outstation = db.Column(db.Boolean, default=False, nullable=True)
    one_way = db.Column(db.Boolean, default=False, nullable=True)
    website = db.relationship('CabWebsite', foreign_keys=website_id)
    slab = db.Column(db.Integer, nullable=True)
    driver_daily_allowance_charge = db.Column(db.DECIMAL, nullable=True)
    driver_per_hr_allowance_charge = db.Column(db.DECIMAL, nullable=True)
    car_night_allowance_charge = db.Column(db.DECIMAL, nullable=True)
    base_fare = db.Column(db.DECIMAL, nullable=True)
    base_fare_weekend = db.Column(db.DECIMAL, nullable=True)
    base_fare_peak_season = db.Column(db.DECIMAL, nullable=True)
    base_fare_with_fuel = db.Column(db.DECIMAL, nullable=True)
    different_pickup_drop_point_charge = db.Column(db.DECIMAL, nullable=True)
    km_restriction = db.Column(db.DECIMAL, nullable=True)
    fare_exceeded_per_hr = db.Column(db.DECIMAL, nullable=True)
    fare_exceeded_per_km = db.Column(db.DECIMAL, nullable=True)
    initial_km = db.Column(db.Integer, nullable=True)
    initial_km_fare = db.Column(db.DECIMAL, nullable=True)
    cancellation_charges = db.Column(db.DECIMAL, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<booking_id %r>' % self.booking_id

    def __hash__(self):
        return hash(self.base_fare)


class CabDealAssociation(Base):
    __tablename__ = 'cab_deal_association'

    cab_id = db.Column(db.Integer, db.ForeignKey('cab.id'))
    deal_id = db.Column(db.Integer, db.ForeignKey('cab_deal.id'))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<cab_id %r>' % self.cab_id