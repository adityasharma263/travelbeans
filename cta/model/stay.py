# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Stay(Base):
    __tablename__ = 'stay'

    title = db.Column(db.String)
    price = db.Column(db.String)
    distance = db.Column(db.String)
    rating = db.Column(db.Float)
    location = db.Column(db.String)
    details = db.Column(db.String)
    image = db.Column(db.String)
    rating_label = db.Column(db.String)
    wifi = db.Column(db.String)
    star = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<title %r>' % self.title