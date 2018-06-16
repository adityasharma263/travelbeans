# -*- coding: utf-8 -*-

from cta.model.room import Room
from cta.model.room import Facility
from cta.model.room import Member
from cta import ma


class MemberSchema(ma.ModelSchema):
    class Meta:
        model = Member
        exclude = ('updated_at', 'created_at')


class FacilitySchema(ma.ModelSchema):
    class Meta:
        model = Facility
        exclude = ('updated_at', 'created_at')


class RoomSchema(ma.ModelSchema):
    member = ma.Nested(MemberSchema, many=False)
    facilities = ma.Nested(FacilitySchema, many=False)
    class Meta:
        model = Room
        exclude = ('updated_at', 'created_at')