# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = db.Column(db.String)
    rating = db.Column(db.Float, nullable=True)
    city = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True, unique=True)
    latitude = db.Column('latitude', db.Float(asdecimal=True), nullable=True)
    longitude = db.Column('longitude', db.Float(asdecimal=True), nullable=True)
    address = db.Column(db.String, nullable=True)
    images = db.relationship('Image', backref='hotel')
    amenities = db.relationship('Amenity', uselist=False, backref='hotel')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<name %r>' % self.name


class Image(Base):
    __tablename__ = 'image'
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    image_url = db.Column(db.String, default=False, nullable=True)
    image_type = db.Column(db.Integer, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<image_url %r>' % self.image_url

class Amenity(Base):
    __tablename__ = 'amenity'
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), unique=True)



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<pool %r>' % self.pool


class Categories(Base):
    __tablename__ = 'categories'
    category = db.Column(db.String, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<category %r>' % self.category


class Cuisines(Base):
    __tablename__ = 'cuisines'
    cuisine = db.Column(db.String, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<cuisine %r>' % self.cuisine


class Cuisines(Base):
    __tablename__ = 'cuisines'
    cuisine = db.Column(db.String, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<cuisine %r>' % self.cuisine


class Collections(Base):
    __tablename__ = 'Collections'
    collection = db.Column(db.String, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<collection %r>' % self.collection


class dishes(Base):
    __tablename__ = 'dishes'
    dish = db.Column(db.String, default=False, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<dish %r>' % self.dish