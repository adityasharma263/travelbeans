# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class WebsiteRoom(Base):
    __tablename__ = 'website_room'

    website_room_id = db.Column(db.Integer,primary_key=True, unique=True, index=True)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    website = db.relationship("Website", backref="room_assocs")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<website_id %r>' % self.website_id