# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Website(Base):
    __tablename__ = 'website'

    website = db.Column(db.String)
    logo_image = db.Column(db.String, nullable=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    rooms = db.relationship('Room', foreign_keys=room_id)
    price = db.relationship('Price', backref='website')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<website %r>' % self.website