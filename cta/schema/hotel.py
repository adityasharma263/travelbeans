# -*- coding: utf-8 -*-

from cta.model.hotel import Hotel
from cta.model.hotel import Image
from cta.schema.room import RoomSchema
from cta.schema.website import WebsiteSchema
from cta.model.hotel import Amenity
from cta import ma


class AmenitySchema(ma.ModelSchema):
    class Meta:
        model = Amenity
        exclude = ('updated_at', 'created_at')

class ImageSchema(ma.ModelSchema):
    class Meta:
        model = Image
        exclude = ('updated_at', 'created_at')


class HotelSchema(ma.ModelSchema):
    amenities = ma.Nested(AmenitySchema, many=False)
    images = ma.Nested(ImageSchema, many=True)
    rooms = ma.Nested(RoomSchema, many=True)
    websites = ma.Nested(WebsiteSchema, many=True)

    class Meta:
        model = Hotel
        exclude = ('updated_at', 'created_at')