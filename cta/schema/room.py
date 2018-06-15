# -*- coding: utf-8 -*-

from cta.model.room import Room
from cta.schema.member import MemberSchema

from cta.schema.website import WebsiteSchema
from cta import ma


class RoomSchema(ma.ModelSchema):
    members = ma.Nested(MemberSchema, many=True)
    websites = ma.Nested(WebsiteSchema, many=True)


    class Meta:
        model = Room
        exclude = ('updated_at', 'created_at')