# -*- coding: utf-8 -*-

from cta.model.hotel import Hotel
from cta.schema.room import RoomSchema
from cta.schema.website import WebsiteSchema
from cta.schema.amenity import AmenitySchema
from cta import ma


class HotelSchema(ma.ModelSchema):
    amenities = ma.Nested(AmenitySchema, many=False)
    rooms = ma.Nested(RoomSchema, many=True)
    websites = ma.Nested(WebsiteSchema, many=True)

    class Meta:
        model = Hotel
        exclude = ('updated_at', 'created_at')