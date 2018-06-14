# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Website(Base):
    __tablename__ = 'website'

    website = db.Column(db.String)
    logo_image = db.Column(db.String, nullable=True)
    hotels = db.relationship('Hotel', backref='website')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<website %r>' % self.website