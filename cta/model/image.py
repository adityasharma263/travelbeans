# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Image(Base):
    __tablename__ = 'image'

    image = db.Column(db.String)
    secondary_images = db.Column(db.String, nullable=True)
    hotels = db.relationship('Hotel', backref='image')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<image %r>' % self.image