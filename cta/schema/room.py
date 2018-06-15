# -*- coding: utf-8 -*-

from cta.model.room import Room
from cta.schema.member import MemberSchema
from cta import ma


class RoomSchema(ma.ModelSchema):
    member = ma.Nested(MemberSchema, many=False)

    class Meta:
        model = Room
        exclude = ('updated_at', 'created_at')