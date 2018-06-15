# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class WebsiteHotel(Base):
    __tablename__ = 'website_hotel'

    website_id = db.Column(db.Integer, db.ForeignKey('website.id'))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
    website = db.relationship("Website", backref="hotel_assocs")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<website_id %r>' % self.website_id