# -*- coding: utf-8 -*-

from cta.model.room import Room
from cta.model.room import Facility
from cta.model.room import Member
from cta import ma
from cta.schema.base import safe_execute


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
    check_in = ma.Method('check_in_epoch')
    check_out = ma.Method('check_out_epoch')

    def check_in_epoch(self, obj):
        return safe_execute(None, ValueError, obj.check_in)

    def check_out_epoch(self, obj):
        return safe_execute(None, ValueError, obj.check_out)

    class Meta:
        model = Room
        exclude = ('updated_at', 'created_at')