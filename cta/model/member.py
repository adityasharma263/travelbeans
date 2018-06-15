# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Member(Base):
    __tablename__ = 'member'

    no_of_adults = db.Column(db.Integer, nullable=True)
    no_of_children = db.Column(db.Integer, nullable=True)
    total_members = db.Column(db.Integer, nullable=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<total_members %r>' % self.total_members