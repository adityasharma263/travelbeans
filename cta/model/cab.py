# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Cab(Base):
    __tablename__ = 'cab'

    car_name = db.Column(db.String)
    city = db.Column(db.String, nullable=True)
    car_type = db.Column(db.Integer, nullable=True)
    cab_type = db.Column(db.Integer, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    bookings = db.relationship('CabBooking', backref='cab')
    images = db.relationship('CabImage', backref='cab')
    amenities = db.relationship('CabAmenity', uselist=False, backref='cab')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<name %r>' % self.name


class CabBooking(Base):
    __tablename__ = 'cab_booking'

    cab_id = db.Column(db.Integer, db.ForeignKey('cab.id'))
    one_way = db.Column(db.Boolean, default=False, nullable=True)
    pickup_time = db.Column(db.DateTime(timezone=True), nullable=False)
    drop_time = db.Column(db.DateTime(timezone=True), nullable=False)
    outstation = db.Column(db.Boolean, default=False, nullable=True)
    drop_latitude = db.Column('drop_latitude', db.Float(asdecimal=True), nullable=True)
    drop_longitude = db.Column('drop_longitude', db.Float(asdecimal=True), nullable=True)
    pickup_latitude = db.Column('pickup_latitude', db.Float(asdecimal=True), nullable=True)
    pickup_longitude = db.Column('pickup_longitude', db.Float(asdecimal=True), nullable=True)
    invoices = db.relationship('CabInvoice', backref='cab_booking')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<cab_id %r>' % self.cab_id


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


class CabInvoice(Base):
    __tablename__ = 'cab_invoice'

    booking_id = db.Column(db.Integer, db.ForeignKey('cab_booking.id'), unique=False)
    website_id = db.Column(db.Integer, db.ForeignKey('cab_website.id'), unique=False)
    websites = db.relationship('CabWebsite', foreign_keys=website_id)
    slab = db.Column(db.Integer, nullable=True)
    driver_night_allowance_charge = db.Column(db.DECIMAL, nullable=True)
    car_night_allowance_charge = db.Column(db.DECIMAL, nullable=True)
    total_hours = db.Column(db.Integer, nullable=True)
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
    distance = db.Column(db.DECIMAL, nullable=True)
    taxes = db.relationship('CabTax', uselist=False, backref='cab_invoice')
    total_fare = db.Column(db.DECIMAL, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<booking_id %r>' % self.booking_id


class CabTax(Base):
    __tablename__ = 'cab_tax'

    invoice_id = db.Column(db.Integer, db.ForeignKey('cab_invoice.id'))
    gst = db.Column(db.DECIMAL, nullable=True)
    s_gst = db.Column(db.DECIMAL, nullable=True)
    c_gst = db.Column(db.DECIMAL, nullable=True)

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
