# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = db.Column(db.String)
    website = db.Column(db.String, nullable=True)
    rating = db.Column(db.DECIMAL, nullable=True)
    nearest_metro_station = db.Column(db.String)
    off_day_in_week = db.Column(db.String)
    opening_time = db.Column(db.TIME(), nullable=True)
    closing_time = db.Column(db.TIME(), nullable=True)
    break_time = db.Column(db.TIME(), nullable=True)
    break_interval = db.Column(db.Integer, nullable=True)
    mode_of_payment = db.Column(db.String, nullable=True)
    especially = db.Column(db.Text, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    city = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True, unique=True)
    latitude = db.Column('latitude', db.Float(asdecimal=True), nullable=True)
    longitude = db.Column('longitude', db.Float(asdecimal=True), nullable=True)
    address = db.Column(db.String, nullable=True)
    locality = db.Column(db.String, nullable=True)
    category = db.Column(db.Integer, nullable=True)
    featured = db.Column(db.Boolean, default=False, nullable=True)
    restaurant_chain_id = db.Column(db.Integer, db.ForeignKey('restaurant_chain.id'), unique=False, nullable=True)
    restaurant_chain = db.relationship('RestaurantChain', foreign_keys=restaurant_chain_id)
    collections = db.relationship('Collection', secondary='restaurant_association')
    cuisines = db.relationship('Cuisine', secondary='restaurant_association')
    images = db.relationship('RestaurantImage', backref='restaurant')
    dishes = db.relationship('Dish', backref='restaurant')
    amenities = db.relationship('RestaurantAmenity', uselist=False, backref='restaurant')
    menus = db.relationship('Menu', uselist=False, backref='restaurant')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<name %r>' % self.name


class RestaurantChain(Base):
    __tablename__ = 'restaurant_chain'

    restaurants = db.relationship('Restaurant')
    restaurant_chain_name = db.Column(db.String)
    restaurant_chain_category = db.Column(db.Integer, nullable=True)
    restaurant_chain_desc = db.Column(db.Text, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<restaurant_chain_name %r>' % self.restaurant_chain_name


class RestaurantImage(Base):
    __tablename__ = 'restaurant_image'

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    image_url = db.Column(db.String, default=False, nullable=True)
    image_type = db.Column(db.Integer, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<image_url %r>' % self.image_url


class RestaurantAmenity(Base):
    __tablename__ = 'restaurant_amenity'

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), unique=True, nullable=False)
    home_delivery = db.Column(db.Boolean, default=False, nullable=True)
    private_dining_area_available = db.Column(db.Boolean, default=False, nullable=True)
    kid_friendly = db.Column(db.Boolean, default=False, nullable=True)
    table_reservation_required = db.Column(db.Boolean, default=False, nullable=True)
    table_booking_recommended = db.Column(db.Boolean, default=False, nullable=True)
    wheelchair_accessible = db.Column(db.Boolean, default=False, nullable=True)
    buffet = db.Column(db.Boolean, default=False, nullable=True)
    wifi = db.Column(db.Boolean, default=False, nullable=True)
    live_entertainment = db.Column(db.Boolean, default=False, nullable=True)
    live_music = db.Column(db.Boolean, default=False, nullable=True)
    live_sports_screening = db.Column(db.Boolean, default=False, nullable=True)
    valet_parking = db.Column(db.Boolean, default=False, nullable=True)
    parking = db.Column(db.Boolean, default=False, nullable=True)
    group_meal = db.Column(db.Boolean, default=False, nullable=True)
    smoking_area = db.Column(db.Boolean, default=False, nullable=True)
    desserts_and_bakes = db.Column(db.Boolean, default=False, nullable=True)
    full_bar_available = db.Column(db.Boolean, default=False, nullable=True)
    serves_jain_food = db.Column(db.Boolean, default=False, nullable=True)
    vegetarian_only = db.Column(db.Boolean, default=False, nullable=True)
    serves_non_veg = db.Column(db.Boolean, default=False, nullable=True)
    nightlife = db.Column(db.Boolean, default=False, nullable=True)
    city_view = db.Column(db.Boolean, default=False, nullable=True)
    brunch = db.Column(db.Boolean, default=False, nullable=True)
    sunday_roast = db.Column(db.Boolean, default=False, nullable=True)
    gastro_pub = db.Column(db.Boolean, default=False, nullable=True)
    beer = db.Column(db.Boolean, default=False, nullable=True)
    outdoor_seating = db.Column(db.Boolean, default=False, nullable=True)
    takeaway = db.Column(db.Boolean, default=False, nullable=True)
    alcohol = db.Column(db.Boolean, default=False, nullable=True)
    seating = db.Column(db.Boolean, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<pool %r>' % self.pool


class Menu(Base):
    __tablename__ = 'menu'
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), unique=True, nullable=False)
    breakfast = db.Column(db.Boolean, default=False, nullable=True)
    lunch = db.Column(db.Boolean, default=False, nullable=True)
    dinner = db.Column(db.Boolean, default=False, nullable=True)
    cafe = db.Column(db.Boolean, default=False, nullable=True)
    lounge = db.Column(db.Boolean, default=False, nullable=True)
    family = db.Column(db.Boolean, default=False, nullable=True)
    bars = db.Column(db.Boolean, default=False, nullable=True)
    nightlife = db.Column(db.Boolean, default=False, nullable=True)
    street_stalls = db.Column(db.Boolean, default=False, nullable=True)
    pocket_friendly = db.Column(db.Boolean, default=False, nullable=True)
    diet = db.Column(db.Boolean, default=False, nullable=True)
    luxury = db.Column(db.Boolean, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<restaurant_id %r>' % self.restaurant_id


class Cuisine(Base):
    __tablename__ = 'cuisine'

    cuisine = db.Column(db.String, default=False, nullable=True)
    featured = db.Column(db.Boolean, default=False, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    image = db.Column(db.String, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<cuisine %r>' % self.cuisine


class Collection(Base):
    __tablename__ = 'collection'

    collection = db.Column(db.String, default=False, nullable=True)
    featured = db.Column(db.Boolean, default=False, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    image = db.Column(db.String, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<collection %r>' % self.collection


class Dish(Base):
    __tablename__ = 'dish'

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    dish = db.Column(db.String, default=False, nullable=True)
    dish_type = db.Column(db.String, nullable=True)
    half_price = db.Column(db.Integer, nullable=True)
    full_price = db.Column(db.Integer, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    image = db.Column(db.String, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<dish %r>' % self.dish


class RestaurantAssociation(Base):
    __tablename__ = 'restaurant_association'

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisine.id'))
    collection = db.relationship('Collection', foreign_keys=collection_id)
    cuisine = db.relationship('Cuisine', foreign_keys=cuisine_id)
    restaurant = db.relationship('Restaurant', foreign_keys=restaurant_id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<restaurant_id %r>' % self.restaurant_id
