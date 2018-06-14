# -*- coding: utf-8 -*-
from cta import db
from cta.model.base import Base


class Member(Base):
    __tablename__ = 'member'

    no_of_adults = db.Column(db.Integer, nullable=True)
    no_of_children= db.Column(db.Integer, nullable=True)
    rooms = db.relationship('Hotel', backref='member')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<no_of_adults %r>' % self.no_of_adults