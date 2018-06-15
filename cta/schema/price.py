# -*- coding: utf-8 -*-

from cta.model.price import Price
from cta.schema.room import RoomSchema
from cta.schema.website import WebsiteSchema
from cta import ma


class PriceSchema(ma.ModelSchema):
    rooms = ma.Nested(RoomSchema, many=False)
    websites = ma.Nested(WebsiteSchema, many=False)

    class Meta:
        model = Price
        exclude = ('updated_at', 'created_at')